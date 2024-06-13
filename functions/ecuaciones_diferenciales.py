import numpy as np
import sympy as sp


def euler(f, a, b, h, co):
    n = int((b - a) / h)
    yeu = [co]
    t = np.linspace(a, b, n + 1)
    for i in range(n):
        yeu.append(yeu[i] + h * f(a + i * h, yeu[i]))
    return yeu, t


def runge_kuta_4(f, a, b, h, co):
    n = int((b - a) / h)
    yeu = [co]
    t = np.linspace(a, b, n + 1)
    for i in range(n):
        k1 = h * f(t[i], yeu[i])
        k2 = h * f(t[i] + h / 2, yeu[i] + k1 / 2)
        k3 = h * f(t[i] + h / 2, yeu[i] + k2 / 2)
        k4 = h * f(t[i + 1], yeu[i] + k3)
        yeu.append(yeu[i] + 1 / 6 * (k1 + 2 * k2 + 2 * k3 + k4))

    return yeu, t


