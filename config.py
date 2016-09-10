"""
>>> class AppConfig(Config):
...     foo = 'foo'
...     def afunc(x, y):
...         return x + y
...
>>> AppConfig.foo
'foo'
>>> AppConfig.foo = 'baz'
>>> AppConfig.foo
'baz'
>>> AppConfig.afunc(1, 2)
3
>>> AppConfig.afunc = lambda x, y: x * y
>>> AppConfig.afunc(1, 2)
2
>>> AppConfig.restore_defaults()
>>> AppConfig.foo
'foo'
>>> AppConfig.afunc(1, 2)
3
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
