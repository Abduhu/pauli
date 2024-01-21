import numpy as np
from math import factorial


def levi_cevita(*args):
    """
    epsilon(a1, a2, ... an) = Prod_{1<= i < j <= n} sgn(aj - ai)
    
    Reference:
    -https://en.wikipedia.org/wiki/Levi-Civita_symbol
    -https://stackoverflow.com/questions/59740966/levi-civita-tensor-in-numpy
    """
    assert 0 not in args, "0 is not an allowed index."

    epsilon = 1
    for i, ai in enumerate(args):
        for j in range(i+1, len(args)):
            epsilon = epsilon * (args[j] - ai)
        epsilon = epsilon / factorial(i)
    return int(round(epsilon, 0))