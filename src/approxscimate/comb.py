import math

import scipy.special as special


def comb(n, k, level=0):
    """
    Calculates the number of ways to choose k items from a set of n distinct items without
    regard to the order of selection. Has different levels of approximation.
    Level=1 indicates an approximated lower bound.
    Level=2 is an approximated higher bound.
    Level=3 is an approximation for large values of n using Stirling's approximation
    :param n: integer
    :param k: integer
    :param level: integer
    :return: integer
    """
    if level == 0:
        return special.comb(n, k)
    if level == 1:
        return (n / k) ** k
    if level == 2:
        return (n ** k) / math.factorial(k)
    if level == 3:
        return (math.sqrt(2 * math.pi * n) * (n / math.e) ** n) / (math.factorial(k) * math.factorial(n - k))
