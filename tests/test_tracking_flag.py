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


def test_progeny():
    assert Alpha.progeny == {  # pragma: no branch
        cls: cls
        for cls in (Bravo, Delta)
    }
    assert Bravo.progeny == {Delta: Delta}
    assert Charlie.progeny == {Delta: Delta}
    assert Delta.progeny == {}


def test_progeny_untracked():
    assert Charlie not in Base.progeny


def test_progeny_get():
    assert Base.progeny.get(Alpha) is Alpha
    assert Base.progeny.get(Bravo) is Bravo
    assert Base.progeny.get(Charlie) is None
    assert Base.progeny.get(Delta) is Delta
