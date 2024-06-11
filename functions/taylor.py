import sympy as sp
import numpy as np
from math import factorial
import matplotlib.pyplot as plt

# Variables

x_0 = sp.symbols('x0')


def taylor(funcion, x0, n):
    x = sp.symbols('x')
    p = 0
    for k in range(n+1):
        derivate = sp.diff(funcion, x, k)
        derivate = sp.lambdify(x, derivate)
        co = derivate(x0) * (x-x0) ** k / factorial(k)
        p += co
    return p


