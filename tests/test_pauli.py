import numpy as np
from pauli import pauli
from pauli.tensors import levi_cevita


def test_involution():
    assert (pauli.x() @ pauli.x() == pauli.i()).all()
    assert (pauli.y() @ pauli.y() == pauli.i()).all()
    assert (pauli.z() @ pauli.z() == pauli.i()).all()
    assert (-1j * pauli.x() @ pauli.y() @ pauli.z() == pauli.i()).all()


def test_determinant():
    assert np.linalg.det(pauli.i()) == 1
    assert np.linalg.det(pauli.x()) == -1
    assert np.linalg.det(pauli.y()) == -1
    assert np.linalg.det(pauli.z()) == -1

def test_trace():
    assert np.trace(pauli.i()) == 2
    assert np.trace(pauli.x()) == 0
    assert np.trace(pauli.y()) == 0
    assert np.trace(pauli.z()) == 0


def test_commutation():
    """
    [si, sj] = Sum_k 2*i levi_cevita(i, j, k) sk
    """
    SIGMA = [pauli.x(), pauli.y(), pauli.z()]
    commute = lambda s1, s2 : s1 @ s2 - s2 @ s1
    
    for i in range(3):
        for j in range(3):
            right = commute(SIGMA[i], SIGMA[j])
            left = 0
            for k in range(3):
                left += 2 * 1j * levi_cevita(i+1, j+1, k+1) * SIGMA[k]
            assert (left == right).all()


def test_anticommutation():
    """
    """
    SIGMA = [pauli.x(), pauli.y(), pauli.z()]
    anticommute = lambda s1, s2 : s1 @ s2 + s2 @ s1
    delta = lambda i, j : 1 if i == j else 0
    
    for i in range(3):
        for j in range(3):
            right = anticommute(SIGMA[i], SIGMA[j])
            left = 2 * delta(i, j) * pauli.i()
            assert (left == right).all()