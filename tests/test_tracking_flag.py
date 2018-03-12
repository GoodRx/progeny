import progeny


class Base(progeny.Base):
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
    assert Alpha.progeny == {Bravo, Delta}
    assert Bravo.progeny == {Delta}
    assert Charlie.progeny == {Delta, }
    assert Delta.progeny == set()


def test_registry():
    assert Charlie not in Base.progeny.registry.keys()


def test_get_progeny_for():
    assert Base.progeny.get(Alpha) is Alpha
    assert Base.progeny.get(Bravo) is Bravo
    assert Base.progeny.get(Charlie) is None
    assert Base.progeny.get(Delta) is Delta
