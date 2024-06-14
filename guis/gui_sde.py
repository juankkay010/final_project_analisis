import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from functions import sistemas_ecuaciones as sde
import sympy as sp

class PaginaSistemasEcuaciones(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.title('Sistemas de Ecuaciones Lineales')
        self.geometry('1366x768')
        self.configure(bg="#ADD8E6")
        self.inicializar_interfaz()

    def inicializar_interfaz(self):
        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 12), background="#ADD8E6")
        style.configure("TButton", font=("Arial", 12), padding=6)
        style.configure("TEntry", font=("Arial", 12), padding=4)
        style.configure("TText", font=("Arial", 12), padding=4)

        label_A = ttk.Label(self, text="Ingrese la matriz A: ")
        label_A.grid(row=0, column=0, padx=10, pady=10)
        self.A = ttk.Entry(self, width=100)
        self.A.grid(row=0, column=1, padx=10, pady=10)

        label_b = ttk.Label(self, text="Ingrese la matriz b: ")
        label_b.grid(row=1, column=0, padx=10, pady=10)
        self.b = ttk.Entry(self, width=100)
        self.b.grid(row=1, column=1, padx=10, pady=10)

        label_tol = ttk.Label(self, text="Ingrese la tolerancia:")
        label_tol.grid(row=2, column=0, padx=10, pady=10)
        self.tol = ttk.Entry(self, width=100)
        self.tol.grid(row=2, column=1, padx=10, pady=10)

        boton_eliminacion_gaussiana = ttk.Button(self, text="Eliminación Gaussiana", command=self.ejecutar_eliminacion_gaussiana)
        boton_eliminacion_gaussiana.grid(row=3, column=0, padx=10, pady=10)

        boton_pivoteo = ttk.Button(self, text="Pivoteo")
        boton_pivoteo.grid(row=3, column=1, padx=10, pady=10)

        boton_gauss_seidel = ttk.Button(self, text="Gauss Seidel", command=self.ejecutar_gauss_seidel)
        boton_gauss_seidel.grid(row=3, column=2, padx=10, pady=10)

        label_resultado = ttk.Label(self, text="Resultado:")
        label_resultado.grid(row=4, column=0, padx=10, pady=10)
        self.resultado = tk.Text(self, height=2, width=100, font=("Arial", 12), wrap="word")
        self.resultado.grid(row=4, column=1, padx=10, pady=10)

    def ejecutar_eliminacion_gaussiana(self):
        A = eval(self.A.get())
        b = eval(self.b.get())

        matriz_A = np.array(A)
        matriz_b = np.array(b)

        resultado = sde.eliminacion_gaussiana(matriz_A, matriz_b)

        self.resultado.delete('1.0', tk.END)
        self.resultado.insert(tk.END, resultado)

    def ejecutar_gauss_seidel(self):
        A = eval(self.A.get())
        b = eval(self.b.get())
        try:
            tol = float(self.tol.get())
        except ValueError:
            tk.messagebox.showerror("Error", "Para este método es necesaria la tolerancia ")

        matriz_A = np.array(A)
        matriz_b = np.array(b)
        xo = np.zeros(len(matriz_b))

        resultado = sde.G_seidel(matriz_A, matriz_b, xo, tol)

        self.resultado.delete('1.0', tk.END)
        self.resultado.insert(tk.END, resultado)

    def ejecutar_pivoteo(self):
        pass



