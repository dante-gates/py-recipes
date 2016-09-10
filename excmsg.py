"""
Classes which inherit this as a metaclass should also inherit from Exception.

Ex.
n    >>> class E(Exception, metaclass=ErrorMeta):
    ...     pass
    ...
    >>> class E(metaclass=ErrorMeta):
    ...     pass
    Traceback (most recent call last):
        ...
    ValueError: E must inherit from Exception

The real beauty of the Error type is when we mix its use with the exc_msg class.
This will allow us to store exception messages as class level attributes that we
can raise!

Ex.
    >>> class Err(Exception, metaclass=ErrorMeta):
    ...     somethingworse = exc_msg('something worse happened')
    ...     somethingbad = exc_msg('something bad happened')
    ...     just_a = 'regular attribute'
    ...
    >>> raise Err.somethingbad
    Traceback (most recent call last):
        ...
    Err: something bad happened

Attributes not decorated as exc_msg are treated as regular attributes.

Ex.
    >>> print(Err.just_a)
    ...
    regular attribute

Note that these class level attributes are of the same time as the class. This
means we can raise them and catch by looking for the class!
Ex.
    >>> try:
    ...     raise Err.somethingworse
    ... except Err as exc:
    ...     print('Caught', repr(exc))
    ...
    Caught Err('something worse happened',)
    >>> raise Err('exception message defined at runtime')
    ...
    Traceback (most recent call last):
        ...
    Err: exception message defined at runtime
"""

import doctest


class ErrorMeta(type):
    """Metaclass for exceptions that allows one to raise class attributes
    decorated as exc_msg from subclasses.
    """
    def __new__(metacls, name, bases, namespace):
        cls = super().__new__(metacls, name, bases, namespace)
        if not issubclass(cls, Exception):
            raise ValueError('%s must inherit from Exception' % name)
        for name, obj in namespace.items():
            if isinstance(obj, exc_msg):
                setattr(cls, name, cls(obj))
        return cls


class exc_msg(str):
    """Decorate class attributes with this class to indicate that the
    attribute should be raisable.
    """

class Error(Exception, metaclass=ErrorMeta):
    """Base class for Exceptions to inherit from. Class attributes decorated
    with exc_msg may be raised and will have same type as class.
    """


if __name__ == '__main__':
    doctest.testmod()
