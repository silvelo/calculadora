from operaciones.resta import restar


def test_resta_positivos():
    assert restar(2, 3) == -1


def test_resta_negativos():
    assert restar(-2, -3) == 1


def test_resta_mixta():
    assert restar(-2, 3) == -5


def test_resta_ceros():
    assert restar(0, 0) == 0
