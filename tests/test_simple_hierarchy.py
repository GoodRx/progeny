import progeny


class Alpha(progeny.Base):
    pass


class Bravo(Alpha):
    pass


class Charlie(Bravo):
    pass


class Delta(Charlie):
    pass


def test_tracked_descendants():
    assert Alpha.progeny == {Bravo, Charlie, Delta}
    assert Bravo.progeny == {Charlie, Delta}
    assert Charlie.progeny == {Delta, }
    assert Delta.progeny == set()


def test_registry():
    assert Alpha.progeny.registry == {
        Bravo: Bravo,
        Charlie: Charlie,
        Delta: Delta,
    }
    assert Bravo.progeny.registry == {
        Charlie: Charlie,
        Delta: Delta,
    }
    assert Charlie.progeny.registry == {
        Delta: Delta,
    }
    assert Delta.progeny.registry == {}


def test_get_progeny_for():
    assert Alpha.progeny.get(Bravo) is Bravo
    assert Alpha.progeny.get(Charlie) is Charlie
    assert Alpha.progeny.get(Delta) is Delta
