import progeny


class Base(progeny.Base):
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


def test_progeny():
    assert Base.progeny == {
        Alpha: Alpha,
        '=Bravo=': Bravo,
        'charlie': Charlie,
        '=Delta=': Delta,
    }
    assert len(Base.progeny) == 4
