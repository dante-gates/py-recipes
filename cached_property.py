"""
Instance properties that only get executed once. Useful for lazy loading of
attributes and guarantees the attribute won't change (unless you explicitly
choose to).

Usage:

>>> import random
>>> class A:
...     @property
...     def f(self):
...         self.rand = random.randint(0, 1_000)
...         return self.rand
>>> a = A(); a.f is a.f
False


>>> import random
>>> class A:
...     @cached_property
...     def f(self):
...         self.rand = random.randint(0, 1_000)
...         return self.rand
>>> a = A()
>>> a.f is a.f
True
>>> a = A()
>>> hasattr(a, 'rand')
False
>>> _ = a.f
>>> hasattr(a, 'rand')
True
"""


import doctest
from functools import lru_cache


def cached_property(fn):
    return property(lru_cache(1)(fn))


if __name__ == '__main__':
    doctest.testmod()
