import numpy as np
from pauli.gates import (
    cx,
    swap,
    i,
    Toffoli,
    Deutsch,
    rx,
    ry,
    rz,
    T
)


def test_cx():
    assert (cx(0) @ cx(0) == np.kron(i(), i())).all()


def test_cx_swap():
    assert (cx(0) @ cx(1) @ cx(0) == swap()).all()


def test_Toffoli():
    assert (Toffoli() @ Toffoli() == np.kron(np.kron(i(), i()), i())).all()


def test_Deutsch():
    assert np.allclose(Deutsch(np.pi/2), Toffoli(), atol=0.000001)


def test_T():
    assert np.allclose(T(), rz(np.pi/4) * np.exp(1j * np.pi / 8), atol=0.00001)