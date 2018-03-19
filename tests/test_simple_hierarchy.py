import progeny


class Alpha(progeny.Base):
    pass


class Bravo(Alpha):
    pass


class Charlie(Bravo):
    pass


class Delta(Charlie):
    pass


def test_progeny():
    assert Alpha.progeny == {
        Bravo: Bravo,
        Charlie: Charlie,
        Delta: Delta,
    }
    assert Bravo.progeny == {
        Charlie: Charlie,
        Delta: Delta,
    }
    assert Charlie.progeny == {
        Delta: Delta,
    }
    assert Delta.progeny == {}


def test_progeny_get():
    assert Alpha.progeny.get(Bravo) is Bravo
    assert Alpha.progeny.get(Charlie) is Charlie
    assert Alpha.progeny.get(Delta) is Delta
