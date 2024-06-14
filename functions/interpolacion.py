import numpy as np
import sympy as sp

x = sp.symbols('x')


def Polinomial_simple(x_data, y_data):
    n = len(x_data)
    A = np.zeros([n, n])

    for i in range(n):
        for j in range(n):
            A[i, 0] = 1
            A[i, j] = A[i, j - 1] * x_data[i]

    xo = np.zeros(n)
    tol = 1e-6
    a_i = np.linalg.solve(A, y_data)

    return a_i


def Poly(xi, a_i):
    P = 0
    for i in range(len(a_i)):
        P = P + a_i[i] * xi ** i
    return P


def Lagrange(xd, yd):
    n = len(xd)
    P = 0
    for i in range(n):
        L = 1
        for j in range(n):
            if (j != i):
                L = L * (x - xd[j]) / (xd[i] - xd[j])
        P = P + L * yd[i]
    Poly = sp.expand(P)
    return Poly


def minimos_cuadrados(x, y):
    m = len(x)
    sum_x = sum(x)
    sum_f = sum(y)
    sum_x_2 = sum(x ** 2)
    sum_f_x = sum(x * y)

    a_0 = (sum_f * sum_x_2 - sum_x * sum_f_x) / (m * sum_x_2 - sum_x ** 2)
    a_1 = (m * sum_f_x - sum_f * sum_x) / (m * sum_x_2 - sum_x ** 2)

    return a_0, a_1
