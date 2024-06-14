import tkinter as tk
from tkinter import ttk
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
        self.geometry("1366x768")
        self.configure(bg="#ADD8E6")
        self.inicializar_interfaz()

    def inicializar_interfaz(self):
        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 12), background="#ADD8E6")
        style.configure("TButton", font=("Arial", 12), padding=6)
        style.configure("TEntry", font=("Arial", 12), padding=4)

        label_funcion = ttk.Label(self, text="Ingrese la función:")
        label_funcion.grid(row=0, column=0, padx=10, pady=10, sticky="e")
        self.funcion = ttk.Entry(self, width=100)
        self.funcion.grid(row=0, column=1, padx=10, pady=10, sticky="w")

        label_grado = ttk.Label(self, text="Ingrese el grado del polinomio:")
        label_grado.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.grado = ttk.Entry(self, width=100)
        self.grado.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        label_inicial = ttk.Label(self, text="Ingrese el valor inicial:")
        label_inicial.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.inicial = ttk.Entry(self, width=100)
        self.inicial.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        self.figura_funcion, self.ejes_funcion = plt.subplots()
        self.canvas_funcion = FigureCanvasTkAgg(self.figura_funcion, master=self)
        self.canvas_widget_funcion = self.canvas_funcion.get_tk_widget()
        self.canvas_widget_funcion.grid(row=4, column=0, padx=10, pady=10)

        self.figura_polinomio, self.ejes_polinomio = plt.subplots()
        self.canvas_polinomio = FigureCanvasTkAgg(self.figura_polinomio, master=self)
        self.canvas_widget_polinomio = self.canvas_polinomio.get_tk_widget()
        self.canvas_widget_polinomio.grid(row=4, column=1, padx=10, pady=10)

        self.texto_polinomio = tk.Text(self, height=10, width=80, font=("Arial", 12), wrap="word")
        self.texto_polinomio.grid(row=5, column=0, columnspan=2, padx=10, pady=10)

        boton_mostrar_valores = ttk.Button(self, text="Calcular polinomio y graficar",
                                          command=lambda: self.ejecutar_taylor(self.funcion.get(), self.grado.get(),
                                                                               self.inicial.get()))
        boton_mostrar_valores.grid(row=3, column=0, columnspan=2, pady=10)

        self.texto_polinomio.delete('1.0', tk.END)

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

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
        self.ejes_funcion.plot(x_vals, y_vals_funcion, label="Función", color="blue")
        self.ejes_funcion.legend()
        self.ejes_funcion.set_title("Función Original")

        # Graficar el polinomio
        self.ejes_polinomio.clear()
        self.ejes_polinomio.plot(x_vals, y_vals_polinomio, label="Polinomio de Taylor", color="red")
        self.ejes_polinomio.legend()
        self.ejes_polinomio.set_title("Polinomio de Taylor")

        self.canvas_funcion.draw()
        self.canvas_polinomio.draw()

if __name__ == "__main__":
    root = tk.Tk()
    app = PaginaTaylor(root)
    root.mainloop()
