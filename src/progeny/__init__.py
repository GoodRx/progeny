from collections.abc import Mapping


class ProgenyMapping(Mapping):
    def __init__(self, data):
        self._data = data

    def __getitem__(self, key):
        return self._data[key]

    def __iter__(self):
        return iter(self._data)

    def __len__(self):
        return len(self._data)


class _BaseMeta(type):
    def __init__(cls, name, bases, dct):
        super().__init__(name, bases, dct)

        # ProgenyBase doesn't need any of this functionality
        if cls.__bases__[0] is object:
            return

        # do not allow tracking flag to be inherited
        if '__progeny_tracked__' not in dct.keys():
            cls.__progeny_tracked__ = True

        # do not allow the key to be inherited
        if '__progeny_key__' not in dct.keys():
            cls.__progeny_key__ = cls._get_progeny_key()

    @property
    def progeny(self):
        descendants = set(self.__subclasses__())
        for s in self.__subclasses__():
            descendants |= set(s.progeny.values())
        return ProgenyMapping(
            {
                each.__progeny_key__: each
                for each in descendants
                if each.__progeny_tracked__
            }
        )


class Base(metaclass=_BaseMeta):
    # TODO: Make child objects ABCs
    __progeny_tracked__ = True

    @classmethod
    def _get_progeny_key(cls):
        return cls
