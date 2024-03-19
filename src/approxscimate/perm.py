import scipy.special as special
import math

def perm(n, k, level=0):
    """
    Calculates the number of ways to arrange k items out of a set of n distinct items,
    where the order of selection matters. Has different levels of accuracy based on the value of level.
    :param n: integer, total number of items
    :param k: integer, number of items to arrange
    :param level: integer, approximation level
    :return: integer or float, number of arrangements
    """
    if level == 0:
        # Scipy's perm function
        return special.perm(n, k)
    elif level == 1:
        # properties of the Gamma function
        return special.gamma(n + 1) / special.gamma(n - k + 1)
    elif level == 2:
        # simplified formulas and mathematical libraries(smaller values of k)
        product = 1
        for i in range(k):
            product *= (n - i)
        return product

# example
n = 100
k = 20
print(perm(n, k, level=0))  
print(perm(n, k, level=1))  
print(perm(n, k, level=2))  
