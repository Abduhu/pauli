r"""
This module includes:
    - Pauli matrices :
        I : pauli.i()
        X : pauli.x()
        Y : pauli.y()
        Z : pauli.z()

    - Pauli rotations :
        RX(theta) : pauli.rx(theta)
        RY(theta) : pauli.ry(theta)
        RZ(theta) : pauli.rz(theta)


"""


import numpy as np


def i() -> 'np.ndarray':
    """
    Pauli identity matrix.
    """
    return np.array(
        [
            [1 + 0j, 0 + 0j],
            [0 + 0j, 1 + 0j]]
    )


def x() -> 'np.ndarray':
    """
    Pauli X matrix.
    """
    return np.array(
        [
            [0 + 0j, 1 + 0j],
            [1 + 0j, 0 + 0j]]
    )


def y() -> 'np.ndarray':
    """
    Pauli Y matrix.
    """
    return np.array(
        [
            [0 + 0j, 0 - 1j],
            [0 + 1j, 0 + 0j]]
    )


def z() -> 'np.ndarray':
    """
    Pauli Z matrix.
    """
    return np.array(
        [
            [1 + 0j, 0 + 0j],
            [0 + 0j, -1 + 0j]]
    )


def rx(theta : float) -> 'np.ndarray':
    """
    Pauli X rotation matrix
        rx = [
                [   cos(theta), -i sin(theta) ],
                [-i sin(theta),    cos(theta) ]
             ]
    """
    return np.cos(theta/2) * i() -1j * np.sin(theta/2) * x()


def ry(theta : float) -> 'np.ndarray':
    """
    Pauli Y rotation matrix
        ry = [
                [ cos(theta), -sin(theta) ],
                [ sin(theta),  cos(theta) ]
             ]
    """
    return np.cos(theta/2) * i() -1j * np.sin(theta/2) * y()


def rz(theta : float) -> 'np.ndarray':
    """
    Pauli Z rotation matrix
        ry = [
                [ exp(-i theta / 2) ,         0         ],
                [         0         , exp(i theta / 2) ]
             ]
    """
    return np.cos(theta/2) * i() -1j * np.sin(theta/2) * z()