from progeny import ProgenyBase


class Alpha(ProgenyBase):
    pass


class Bravo(Alpha):
    pass


class Charlie(Bravo):
    pass


class Delta(Charlie):
    pass


def test_tracked_descendants():
    assert Alpha.tracked_descendants() == {Bravo, Charlie, Delta}
    assert Bravo.tracked_descendants() == {Charlie, Delta}
    assert Charlie.tracked_descendants() == {Delta, }
    assert Delta.tracked_descendants() == set()


def test_registry():
    assert Alpha._progeny_registry() == {
        Bravo: Bravo,
        Charlie: Charlie,
        Delta: Delta,
    }
    assert Bravo._progeny_registry() == {
        Charlie: Charlie,
        Delta: Delta,
    }
    assert Charlie._progeny_registry() == {
        Delta: Delta,
    }
    assert Delta._progeny_registry() == {}


def test_get_progeny():
    assert Alpha.get_progeny(Bravo) is Bravo
    assert Alpha.get_progeny(Charlie) is Charlie
    assert Alpha.get_progeny(Delta) is Delta