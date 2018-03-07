from progeny import ProgenyBase


class Base(ProgenyBase):
    pass


class Alpha(Base):
    __progeny_key__ = 'alpha'


class Bravo(Alpha):
    __progeny_key__ = 'bravo'


class Charlie(Bravo):
    # purposefully has no key
    pass


class Delta(Charlie):
    __progeny_key__ = 'delta'


def test_tracked_descendants():
    assert Alpha.tracked_descendants() == {Bravo, Charlie, Delta}
    assert Bravo.tracked_descendants() == {Charlie, Delta}
    assert Charlie.tracked_descendants() == {Delta, }
    assert Delta.tracked_descendants() == set()


def test_registry():
    assert Base._progeny_registry() == {
        'alpha': Alpha,
        'bravo': Bravo,
        Charlie: Charlie,
        'delta': Delta,
    }


def test_get_progeny():
    assert Base.get_progeny('alpha') is Alpha
    assert Base.get_progeny('bravo') is Bravo
    assert Base.get_progeny(Charlie) is Charlie
    assert Base.get_progeny('delta') is Delta