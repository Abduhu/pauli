from pauli.tensors import levi_cevita


def test_levi_cevita():
    assert levi_cevita(1, 2, 3) == 1
    assert levi_cevita(2, 1, 3) == -1
    assert levi_cevita(2, 3, 1) == 1
    assert levi_cevita(3, 2, 1) == -1
    assert levi_cevita(3, 1, 2) == 1
    assert levi_cevita(1, 3, 2) == -1
    assert levi_cevita(1, 2, 3, 4) == 1