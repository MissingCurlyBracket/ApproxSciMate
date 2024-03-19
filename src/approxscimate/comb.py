import scipy.special as special
import math


def comb(n, k, level=0):
    """
    Calculates the number of ways to choose k items from a set of n distinct items without
    regard to the order of selection. Has different levels of accuracy based on value of level.
    (Check package documentation for more details)
    :param n: integer
    :param k: integer
    :param level: integer
    :return: integer
    """
    if level == 0:
        return special.comb(n, k)
    if level == 1:
        return (special.gamma(n + 1)) / (special.gamma(k + 1) * special.gamma(n - k + 1))
    if level == 2:
        return (n ** k) / math.factorial(k)
