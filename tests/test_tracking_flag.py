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
    assert Charlie not in Base.progeny_registry.keys()


def test_get_progeny_for():
    assert Base.get_progeny_for(Alpha) is Alpha
    assert Base.get_progeny_for(Bravo) is Bravo
    assert Base.get_progeny_for(Charlie) is None
    assert Base.get_progeny_for(Delta) is Delta
