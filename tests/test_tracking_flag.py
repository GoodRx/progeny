from progeny import ProgenyBase


class Base(ProgenyBase):
    pass


class Alpha(Base):
    pass


class Bravo(Alpha):
    pass


class Charlie(Bravo):
    __progeny_tracked__ = False


class Delta(Charlie):
    pass


def test_tracked_descendants():
    assert Alpha.tracked_descendants() == {Bravo, Delta}
    assert Bravo.tracked_descendants() == {Delta}
    assert Charlie.tracked_descendants() == {Delta, }
    assert Delta.tracked_descendants() == set()


def test_registry():
    assert Charlie not in Base._progeny_registry().keys()


def test_get_progeny():
    assert Base.get_progeny(Alpha) is Alpha
    assert Base.get_progeny(Bravo) is Bravo
    assert Base.get_progeny(Charlie) is None
    assert Base.get_progeny(Delta) is Delta
