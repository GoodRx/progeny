import six


class _BaseMeta(type):
    def __init__(cls, name, bases, dct):
        super(_BaseMeta, cls).__init__(name, bases, dct)

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
            descendants |= s.progeny
        return {
            each for each in descendants
            if each.__progeny_tracked__
        }

    @property
    def progeny_registry(self):
        return {
            each.__progeny_key__: each
            for each in self.progeny
        }


@six.add_metaclass(_BaseMeta)
class Base(object):
    # TODO: Make child objects ABCs
    __progeny_tracked__ = True

    @classmethod
    def _get_progeny_key(cls):
        return cls

    @classmethod
    def get_progeny_for(cls, key):
        """Given a key, return the tracked subclassed"""
        return cls.progeny_registry.get(key)
