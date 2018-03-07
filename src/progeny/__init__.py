class _BaseMeta(type):
    def __new__(meta, name, bases, dct):
        # if attr is not explicitly set, force to None (overriding inheritance)
        dct['__progeny_key__'] = dct.get('__progeny_key__')

        # if attr is not explicitly set, force to True (overriding inheritance)
        if '__progeny_tracked__' not in dct.keys():
            dct['__progeny_tracked__'] = True

        return super(_BaseMeta, meta).__new__(meta, name, bases, dct)

    def __init__(cls, name, bases, dct):

        is_base = cls.__bases__[0] is not object

        if is_base and cls.__progeny_key__ is None:
            cls.__progeny_key__ = cls

        super(_BaseMeta, cls).__init__(name, bases, dct)


class ProgenyBase(object):
    # TODO: Make child objects ABCs
    __metaclass__ = _BaseMeta
    __progeny_tracked__ = True
    # TODO: Allow the key to be defined from a callable
    __progeny_key__ = None

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
