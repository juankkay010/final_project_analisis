import numpy as np


def eliminacion_gaussiana(A, b):
    n = len(b)
    x = np.zeros(n)

    for k in range(0, n - 1):
        for i in range(k + 1, n):
            lambd = A[i, k] / (A[k, k])
            A[i, k:n] = A[i, k:n] - lambd * A[k, k:n]
            b[i] = b[i] - lambd * b[k]

    for k in range(n - 1, -1, -1):
        x[k] = (b[k] - np.dot(A[k, k + 1:n], x[k + 1:n])) / A[k, k]

    return x


def G_seidel(A, b, xo, tol):
    D = np.diag(np.diag(A))
    U = D - np.triu(A)
    L = D - np.tril(A)
    Tg = np.dot(np.linalg.inv((D - L)), U)
    Cg = np.dot(np.linalg.inv((D - L)), b)
    lam, v = np.linalg.eig(Tg)
    contador = 1
    lista = []

    if max(abs(lam)) < 1:
        x1 = np.dot(Tg, xo) + Cg

        while max(abs(x1 - xo)) > tol:
            lista.append((x1, (max(abs(x1 - xo)))))
            xo = x1
            x1 = np.dot(Tg, xo) + Cg
            contador += 1

        lista.append((x1, (max(abs(x1 - xo)))))

        return x1

    else:
        print(f'El sistema iterativo  con vector inicial {xo} no converge')


def gauss_seidel_sumatorias(A, b, xo, tol, max_iter=100):
    n = len(b)
    x1 = np.zeros(n)
    norm = 2  # Inicialmente mayor que la tolerancia
    cont = 0

    while norm > tol and cont < max_iter:
        for i in range(n):
            aux = 0
            for j in range(n):
                if i != j:
                    aux -= A[i, j] * xo[j]
            x1[i] = (b[i] + aux) / A[i, i]

        norm = np.max(np.abs(x1 - xo))
        xo = x1.copy()
        cont += 1

    return x1
