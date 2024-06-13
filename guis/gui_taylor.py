import tkinter as tk
import sympy as sp
from functions import taylor
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from tkinter import messagebox


class PaginaTaylor(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.title("Series de Taylor")
        self.geometry("1300x850")
        self.inicializar_interfaz()

    def inicializar_interfaz(self):
        label_funcion = tk.Label(self, text="Ingrese la función:")
        label_funcion.grid(row=0, column=0, padx=5, pady=5)
        self.funcion = tk.Entry(self)
        self.funcion.grid(row=0, column=1, padx=5, pady=5)

        label_grado = tk.Label(self, text="Ingrese el grado del polinomio:")
        label_grado.grid(row=1, column=0, padx=5, pady=5)
        self.grado = tk.Entry(self)
        self.grado.grid(row=1, column=1, padx=5, pady=5)

        label_inicial = tk.Label(self, text="Ingrese el valor inicial:")
        label_inicial.grid(row=2, column=0, padx=5, pady=5)
        self.inicial = tk.Entry(self)
        self.inicial.grid(row=2, column=1, padx=5, pady=5)

        self.figura_funcion, self.ejes_funcion = plt.subplots()
        self.canvas_funcion = FigureCanvasTkAgg(self.figura_funcion, master=self)
        self.canvas_widget_funcion = self.canvas_funcion.get_tk_widget()
        self.canvas_widget_funcion.grid(row=4, column=0, padx=5, pady=5)

        self.figura_polinomio, self.ejes_polinomio = plt.subplots()
        self.canvas_polinomio = FigureCanvasTkAgg(self.figura_polinomio, master=self)
        self.canvas_widget_polinomio = self.canvas_polinomio.get_tk_widget()
        self.canvas_widget_polinomio.grid(row=4, column=1, padx=5, pady=5)

        self.texto_polinomio = tk.Text(self, height=10, width=50)
        self.texto_polinomio.grid(row=5, columnspan=2, padx=5, pady=5)

        boton_mostrar_valores = tk.Button(self, text="Calcular polinomio y graficar",
                                          command=lambda: self.ejecutar_taylor(self.funcion.get(), self.grado.get(),
                                                                               self.inicial.get()))
        boton_mostrar_valores.grid(row=3, columnspan=2, pady=10)

        self.texto_polinomio.delete('1.0', tk.END)

    def ejecutar_taylor(self, funcion, grado, inicial):
        try:
            funcion = sp.sympify(funcion)
        except (sp.SympifyError, TypeError):
            tk.messagebox.showerror("Error", "La función ingresada no es válida")
            return

        try:
            grado = int(grado)
        except ValueError:
            tk.messagebox.showerror("Error", "El grado debe ser un número entero")
            return

        try:
            inicial = int(inicial)
        except ValueError:
            tk.messagebox.showerror("Error", "El valor inicial debe ser un número entero")
            return

        resultado = taylor.taylor(funcion, inicial, grado)

        self.texto_polinomio.delete('1.0', tk.END)
        self.texto_polinomio.insert(tk.END, str(resultado))
        self.graficas(funcion, resultado, inicial)

    def graficas(self, funcion, polinomio, inicial):
        x = sp.symbols('x')
        funcion = sp.lambdify(x, funcion)
        polinomio = sp.lambdify(x, polinomio)

        x_vals = np.linspace(inicial - 10, inicial + 10, 100)
        y_vals_funcion = funcion(x_vals)
        y_vals_polinomio = polinomio(x_vals)

        # Graficar la función
        self.ejes_funcion.clear()
        self.ejes_funcion.plot(x_vals, y_vals_funcion, label="Función")
        self.ejes_funcion.legend()
        self.canvas_funcion.draw()

        # Graficar el polinomio
        self.ejes_polinomio.clear()
        self.ejes_polinomio.plot(x_vals, y_vals_polinomio, label="Polinomio")
        self.ejes_polinomio.legend()
        self.canvas_polinomio.draw()

