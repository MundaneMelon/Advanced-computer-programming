"""
This tutorial demonstrates the use of
functions as arguments
"""


def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1

    return total


def cube(x):
    return x * x * x


def sum_cubes(n):
    return summation(n, cube)


print(sum_cubes(3))
