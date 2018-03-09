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
    assert Alpha.progeny_registry == {
        Bravo: Bravo,
        Charlie: Charlie,
        Delta: Delta,
    }
    assert Bravo.progeny_registry == {
        Charlie: Charlie,
        Delta: Delta,
    }
    assert Charlie.progeny_registry == {
        Delta: Delta,
    }
    assert Delta.progeny_registry == {}


def test_get_progeny_for():
    assert Alpha.get_progeny_for(Bravo) is Bravo
    assert Alpha.get_progeny_for(Charlie) is Charlie
    assert Alpha.get_progeny_for(Delta) is Delta
