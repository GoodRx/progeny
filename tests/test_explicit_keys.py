import pytest

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


def test_progeny():
    assert Alpha.progeny == {
        'bravo': Bravo,
        Charlie: Charlie,
        'delta': Delta,
    }
    assert Bravo.progeny == {
        Charlie: Charlie,
        'delta': Delta,
    }
    assert Charlie.progeny == {
        'delta': Delta,
    }
    assert Delta.progeny == {}


def test_base_progeny():
    assert Base.progeny == {
        'alpha': Alpha,
        'bravo': Bravo,
        Charlie: Charlie,
        'delta': Delta,
    }


def test_base_progeny_items():
    def sort_key(keyval):
        _, val = keyval
        return str(val)

    assert sorted(Base.progeny.items(), key=sort_key) == sorted([
        ('alpha', Alpha),
        ('bravo', Bravo),
        (Charlie, Charlie),
        ('delta', Delta),
    ], key=sort_key)


def test_progeny_immutable():
    with pytest.raises(TypeError):
        Base.progeny['new'] = 1

    for key in Base.progeny:
        with pytest.raises(TypeError):
            del Base.progeny[key]


def test_progeny_get():
    assert Base.progeny.get('alpha') is Alpha
    assert Base.progeny.get('bravo') is Bravo
    assert Base.progeny.get(Charlie) is Charlie
    assert Base.progeny.get('delta') is Delta
