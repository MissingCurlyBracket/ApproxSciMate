import numpy as np
import math

def cbrt_approx(x, level=0):
    """
    Approximates the cube root of each element in the input array x with different levels of accuracy.
    :param x: array-like
    :param level: integer (0, 1, or 2)
    :return: array-like
    """
    result = []
    for elem in x:
        if level == 0:
            result.append(np.cbrt(elem))  # Level 0: Use numpy's cbrt function for highest accuracy
        elif level == 1:
            result.append(elem ** (1/3))   # Level 1: Use simple exponentiation for moderate accuracy
        elif level == 2:
            result.append(approx_cbrt(elem))  # Level 2: Use a simple approximation function for lower accuracy
    return result

def approx_cbrt(x):
    """
    Simple approximation of cube root using Newton's method.
    """
    guess = x / 3
    for _ in range(10):  # Adjust as needed for desired accuracy
        guess = guess - (guess ** 3 - x) / (3 * guess ** 2)
    return guess

# Example usage:
input_array = [8, 27, 64, 125]  # Example input array
result_level_0 = cbrt_approx(input_array, level=0)
result_level_1 = cbrt_approx(input_array, level=1)
result_level_2 = cbrt_approx(input_array, level=2)
print("Approximation Level 0:", result_level_0)
print("Approximation Level 1:", result_level_1)
print("Approximation Level 2:", result_level_2)

