import numpy as np
import sympy as sp


def biseccion(f, a, b, tol):
    c = None  # "No cumple el teorema"
    i = 0
    while not abs(b - a) < tol:
        i += 1
        c = (a + b) / 2
        if f(c) * f(b) < 0:
            a = c
        elif f(a) * f(c) < 0:
            b = c
    print(f"Iteraciones por Biseccion: {i}")
    return c


def posicion_falsa(f, a, b, tol):
    if f(a) * f(b) > 0:
        i = None
        print(f"La funcion no cumple el teorema en [{a}, {b}]")
        return ""
    else:
        c = a - f(a)*(a - b) / (f(a) - f(b))
        i = 1
        while abs(f(c)) > tol:
            i += 1
            c = a - f(a)*(a - b) / (f(a) - f(b))
            if f(a) * f(c) < 0:
                b = c
            else:
                a = c
    print(f"Iteraciones por Posicion Falsa: {i}")
    return c


def newton(f, x0, tol):
    x = sp.symbols("x")
    i = 1
    df = sp.diff(f, x)
    N = x - f / df
    N = sp.lambdify(x, N)
    x1 = N(x0)
    while abs(x1 - x0) > tol:
        x0 = x1
        x1 = N(x0)
        i += 1

    print(f"Iteraciones por Newton: {i}")

    return x1


def secante(f, a, b, tol):
    i = 0
    while not abs(b - a) < tol:
        i += 1
        fb = f(b)
        c = b - fb * (a - b) / (f(a) - fb)
        a = b
        b = c
    print(f"Iteraciones por Secante: {i}")
    return b
