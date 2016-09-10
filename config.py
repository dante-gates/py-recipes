"""
>>> class AppConfig(Config):
...     foo = 'foo'
...     def afunc(x, y):
...         return x + y
...     alist = [1, 2, 3]
...     adict = {1: 'one', 2: 'two'}
...

Confirming the default values are set normally...

>>> AppConfig.foo
'foo'
>>> AppConfig.afunc(1, 2)
3
>>> AppConfig.alist
[1, 2, 3]
>>> AppConfig.adict
{1: 'one', 2: 'two'}

We can now alter each attribute...

>>> AppConfig.foo = 'baz'
>>> AppConfig.foo
'baz'

>>> AppConfig.afunc = lambda x, y: x - y
>>> AppConfig.afunc(1, 2)
-1

>>> AppConfig.alist.extend([4, 5, 6])
>>> AppConfig.alist
[1, 2, 3, 4, 5, 6]

>>> AppConfig.adict[1] = 'zero'
>>> AppConfig.adict[3] = 'three'
>>> AppConfig.adict
{1: 'zero', 2: 'two', 3: 'three'}

Now we can ask our class to restore its default settings...

>>> AppConfig.restore_defaults()
>>> AppConfig.foo
'foo'
>>> AppConfig.afunc(1, 2)
3
>>> AppConfig.alist
[1, 2, 3]
>>> AppConfig.adict
{1: 'one', 2: 'two'}
"""

import doctest


class ConfigMeta(type):
    def __new__(metacls, name, bases, namespace):
        cls = super().__new__(metacls, name, bases, namespace)
        dft = {}
        for k, v in namespace.items():
            dft[k] = v
        cls._dft = dft
        return cls


class Config(metaclass=ConfigMeta):
    @classmethod
    def restore_defaults(cls):
        for k, v in cls._dft.items():
            setattr(cls, k, v)


if __name__ == '__main__':
    doctest.testmod()
