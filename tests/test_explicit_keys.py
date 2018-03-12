import progeny


class Base(progeny.Base):
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
    assert Alpha.progeny == {Bravo, Charlie, Delta}
    assert Bravo.progeny == {Charlie, Delta}
    assert Charlie.progeny == {Delta, }
    assert Delta.progeny == set()


def test_registry():
    assert Base.progeny.registry == {
        'alpha': Alpha,
        'bravo': Bravo,
        Charlie: Charlie,
        'delta': Delta,
    }


def test_get_progeny_for():
    assert Base.progeny.get('alpha') is Alpha
    assert Base.progeny.get('bravo') is Bravo
    assert Base.progeny.get(Charlie) is Charlie
    assert Base.progeny.get('delta') is Delta
