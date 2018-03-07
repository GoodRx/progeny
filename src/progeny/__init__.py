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


@six.add_metaclass(_BaseMeta)
class ProgenyBase(object):
    # TODO: Make child objects ABCs
    __progeny_tracked__ = True

    @classmethod
    def _get_progeny_key(cls):
        return cls

    @classmethod
    def tracked_descendants(cls):
        rv = set(cls.__subclasses__())
        for s in cls.__subclasses__():
            rv |= s.tracked_descendants()
        return {each for each in rv if each.__progeny_tracked__}

    @classmethod
    def _progeny_registry(cls):
        return {
            each.__progeny_key__: each
            for each in cls.tracked_descendants()
        }

    @classmethod
    def get_progeny(cls, key):
        """Given a key, return the tracked subclassed"""
        return cls._progeny_registry().get(key)
