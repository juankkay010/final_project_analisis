import tkinter as tk
from tkinter import ttk, messagebox
import sympy as sp
from functions import interpolacion as inter
import numpy as np


class PaginaInterpolacion(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.title("Interpolación Polinomial")
        self.geometry("1366x768")
        self.configure(bg="#ADD8E6")
        self.inicializar_interfaz()
        self.x = sp.symbols('x')

    def inicializar_interfaz(self):
        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 12), background="#ADD8E6")
        style.configure("TButton", font=("Arial", 12), padding=6)
        style.configure("TEntry", font=("Arial", 12), padding=4)
        style.configure("TText", font=("Arial", 12), padding=4)

        label_xdata = ttk.Label(self, text="Datos de x:")
        label_xdata.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.xdata = ttk.Entry(self, width=100)
        self.xdata.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        label_ydata = ttk.Label(self, text="Datos de y:")
        label_ydata.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.ydata = ttk.Entry(self, width=100)
        self.ydata.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        label_dato = ttk.Label(self, text="Valor a aproximar:")
        label_dato.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.dato = ttk.Entry(self, width=100)
        self.dato.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        boton_poly = ttk.Button(self, text="Polinomial Simple", command=self.ejecutar_polinomial_simple)
        boton_poly.grid(row=4, column=0, padx=10, pady=10)

        boton_lagrange = ttk.Button(self, text="Lagrange", command=self.ejecutar_lagrange)
        boton_lagrange.grid(row=4, column=1, padx=10, pady=10)

        boton_cuadrados = ttk.Button(self, text="Mínimos Cuadrados", command=self.ejecutar_minimos_cuadrados)
        boton_cuadrados.grid(row=4, column=2, padx=10, pady=10)

        label_polinomio = ttk.Label(self, text="Polinomio:")
        label_polinomio.grid(row=6, column=0, padx=10, pady=10, sticky="e")
        self.polinomio = tk.Text(self, height=2, width=100, font=("Arial", 12), wrap="word")
        self.polinomio.grid(row=6, column=1, padx=10, pady=10, sticky="w")

        label_resultado = ttk.Label(self, text="Dato aproximado:")
        label_resultado.grid(row=7, column=0, padx=10, pady=10, sticky="e")
        self.resultado = tk.Text(self, height=2, width=100, font=("Arial", 12), wrap="word")
        self.resultado.grid(row=7, column=1, padx=10, pady=10, sticky="w")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=3)

    def ejecutar_polinomial_simple(self):
        try:
            xdata = list(map(float, self.xdata.get().split(',')))
            ydata = list(map(float, self.ydata.get().split(',')))
            dato = float(self.dato.get())
            polinomio_matriz = inter.Polinomial_simple(xdata, ydata)
            polinomio = inter.Poly(self.x, polinomio_matriz)
            dato_aproximado = inter.Poly(dato, polinomio_matriz)
        except ValueError as e:
            tk.messagebox.showerror("Error", f"Error en los datos ingresados: {e}")
            return
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error inesperado: {e}")
            return

        self.polinomio.delete('1.0', tk.END)
        self.polinomio.insert(tk.END, polinomio)
        self.resultado.delete('1.0', tk.END)
        self.resultado.insert(tk.END, dato_aproximado)

    def ejecutar_minimos_cuadrados(self):
        try:
            xdata = np.array(list(map(float, self.xdata.get().split(','))))
            ydata = np.array(list(map(float, self.ydata.get().split(','))))
            dato = float(self.dato.get())
            b, m = inter.minimos_cuadrados(xdata, ydata)
            modelo = lambda x: m * x + b
            dato_aproximado = modelo(dato)
        except ValueError as e:
            tk.messagebox.showerror("Error", f"Error en los datos ingresados: {e}")
            return
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error inesperado: {e}")
            return

        self.polinomio.delete('1.0', tk.END)
        self.polinomio.insert(tk.END, f"{m}*x+{b}")
        self.resultado.delete('1.0', tk.END)
        self.resultado.insert(tk.END, dato_aproximado)

    def ejecutar_lagrange(self):
        try:
            xdata = np.array(list(map(float, self.xdata.get().split(','))))
            ydata = np.array(list(map(float, self.ydata.get().split(','))))
            dato = float(self.dato.get())
            polinomio = inter.Lagrange(xdata, ydata)
            poly = sp.lambdify(self.x, polinomio)
            dato_aproximado = poly(dato)
        except ValueError as e:
            tk.messagebox.showerror("Error", f"Error en los datos ingresados: {e}")
            return
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error inesperado: {e}")
            return

        self.polinomio.delete('1.0', tk.END)
        self.polinomio.insert(tk.END, polinomio)
        self.resultado.delete('1.0', tk.END)
        self.resultado.insert(tk.END, dato_aproximado)


