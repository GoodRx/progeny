from progeny import ProgenyBase


class Base(ProgenyBase):
    pass


class Alpha(Base):
    pass


class Bravo(Alpha):
    @classmethod
    def _get_progeny_key(cls):
        return '={}='.format(cls.__name__)


class Charlie(Bravo):
    __progeny_key__ = 'charlie'


class Delta(Charlie):
    pass


def test_registry():
    assert Base._progeny_registry() == {
        Alpha: Alpha,
        '=Bravo=': Bravo,
        'charlie': Charlie,
        '=Delta=': Delta,
    }
