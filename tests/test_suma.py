from operaciones.suma import suma


def test_suma_positivos():
    assert suma(2, 3) == 5


def test_suma_negativos():
    assert suma(-2, -3) == -5


def test_suma_mixta():
    assert suma(-2, 3) == 1


def test_suma_ceros():
    assert suma(0, 0) == 0
