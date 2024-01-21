import numpy as np
from pauli import pauli


def cx(control=0):
    """
    Assume two qubit 0 and 1
        cx(control=0) : qubit 0 is the controlling qubit
        cx(control=1) : qubit 1 is the controlling qubit
    inputs:
        control : controlling qubit
    """
    if not control:
        return np.array(
            [
                [1, 0, 0, 0],
                [0, 1, 0, 0],
                [0, 0, 0, 1],
                [0, 0, 1, 0]
            ]
        )
    else:
        return np.array(
            [
                [1, 0, 0, 0],
                [0, 0, 0, 1],
                [0, 0, 1, 0],
                [0, 1, 0, 0]
            ]
        )


def swap():
    """
    """
    return np.array(
        [
            [1, 0, 0, 0],
            [0, 0, 1, 0],
            [0, 1, 0, 0],
            [0, 0, 0, 1]
        ]
    )


def Deutsch(theta):
    """
    Deutsch gate
    """
    return np.array(
        [
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 1j * np.cos(theta),      np.sin(theta)],
            [0, 0, 0, 0, 0, 0,      np.sin(theta), 1j * np.cos(theta)],
        ]
    )


def Toffoli():
    """
    Toffoli gate
    """
    return np.array(
        [
            [1, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0, 1, 0],
        ]
    )


def T():
    return np.array(
        [
            [1, 0],
            [0, np.exp(1j * np.pi / 4)]
        ]
    )


def x():
    return pauli.x()


def y():
    return pauli.y()


def z():
    return pauli.z()


def i():
    return pauli.i()


def rx(theta):
    return pauli.rx(theta)


def ry(theta):
    return pauli.ry(theta)


def rz(theta):
    return pauli.rz(theta)


def NOT():
    return pauli.x()