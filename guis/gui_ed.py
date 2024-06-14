import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from functions import ecuaciones_diferenciales as ed
import sympy as sp


class PaginaEcuacionesDiferenciales(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.title('Ecuaciones diferenciales')
        self.geometry('1366x768')
        self.ecuaciones = []
        self.configure(bg="#ADD8E6")
        self.inicializar_interfaz()

    def inicializar_interfaz(self):
        style = ttk.Style()
        style.configure("TLabel", font=("Arial", 12), background="#ADD8E6")
        style.configure("TButton", font=("Arial", 12), padding=6)
        style.configure("TEntry", font=("Arial", 12), padding=4)
        style.configure("TText", font=("Arial", 12), padding=4)

        label_ecuacion1 = ttk.Label(self, text="Ingrese la primera ecuación diferencial:")
        label_ecuacion1.grid(row=6, column=0, padx=5, pady=5)
        self.ecuacion1 = tk.Entry(self)
        self.ecuacion1.grid(row=6, column=1, padx=5, pady=5)

        label_ecuacion2 = ttk.Label(self, text="Ingrese la segunda ecuación diferencial:")
        label_ecuacion2.grid(row=7, column=0, padx=5, pady=5)
        self.ecuacion2 = tk.Entry(self)
        self.ecuacion2.grid(row=7, column=1, padx=5, pady=5)

        label_intervalo = ttk.Label(self, text="Ingrese el intervalo [a,b]:")
        label_intervalo.grid(row=2, column=0, padx=5, pady=5)
        self.intervalo = tk.Entry(self)
        self.intervalo.grid(row=2, column=1, padx=5, pady=5)

        label_h = ttk.Label(self, text="Ingrese h:")
        label_h.grid(row=3, column=0, padx=5, pady=5)
        self.h = tk.Entry(self)
        self.h.grid(row=3, column=1, padx=5, pady=5)

        label_condiciones_iniciales = ttk.Label(self, text="Ingrese la condición inicial:")
        label_condiciones_iniciales.grid(row=4, column=0, padx=5, pady=5)
        self.condiciones_iniciales = tk.Entry(self)
        self.condiciones_iniciales.grid(row=4, column=1, padx=5, pady=5)

        boton_euler = ttk.Button(self, text="Método Euler", command=lambda:self.uno_o_dos_euler(self.intervalo.get(),
                                                                                               self.h.get(),
                                                                                               self.condiciones_iniciales.get(),))

        boton_runge_kuta = ttk.Button(self, text="Método Runge Kuta", command=lambda: self.uno_o_dos_runge(self.intervalo.get(),
                                                                                                self.h.get(),
                                                                                                self.condiciones_iniciales.get(), ))


        boton_euler.grid(row=1, column=0, padx=5, pady=5)
        boton_runge_kuta.grid(row=1, column=1, padx=5, pady=5)

        self.figura_ecuacion, self.ejes_ecuacion = plt.subplots()
        self.canvas_ecuacion = FigureCanvasTkAgg(self.figura_ecuacion, master=self)
        self.canvas_widget_ecuacion = self.canvas_ecuacion.get_tk_widget()
        self.canvas_widget_ecuacion.grid(row=0, column=0, columnspan=2, padx=5, pady=5)

        #self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=2)
        self.grid_columnconfigure(1, weight=2)

    def ejecutar_euler_primer_orden(self, ecuacion, intervalo, h, condiciones_iniciales):
        try:
            y, t = sp.symbols('y t')

            # Conversion de datos
            ecuacion = sp.sympify(ecuacion)
            lambd = sp.lambdify((t, y), ecuacion)
            intervalo = intervalo.split(',')
            a = float(intervalo[0])
            b = float(intervalo[1])
            h = float(h)
            condiciones_iniciales = float(condiciones_iniciales)

            yeu, tiempo = ed.euler(lambd, a, b, h, condiciones_iniciales)
        except ValueError as e:
            tk.messagebox.showerror("Error", f"Error en los datos ingresados: {e}")
            return
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error inesperado: {e}")
            return

        self.ejes_ecuacion.clear()
        self.ejes_ecuacion.plot(tiempo, yeu)
        self.canvas_ecuacion.draw()

    def ejecutar_runge_kuta_primer_orden(self, ecuacion, intervalo, h, condiciones_iniciales):
        try:
            y, t = sp.symbols('y t')

            # Conversion de datos
            ecuacion = sp.sympify(ecuacion)
            lambd = sp.lambdify((t, y), ecuacion)
            intervalo = intervalo.split(',')
            a = float(intervalo[0])
            b = float(intervalo[1])
            h = float(h)
            condiciones_iniciales = float(condiciones_iniciales)

            yeu, tiempo = ed.runge_kuta_4(lambd, a, b, h, condiciones_iniciales)
        except ValueError as e:
            tk.messagebox.showerror("Error", f"Error en los datos ingresados: {e}")
            return
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error inesperado: {e}")
            return

        self.ejes_ecuacion.clear()
        self.ejes_ecuacion.plot(tiempo, yeu)
        self.canvas_ecuacion.draw()

    def ecuaciones_orden_superior_euler(self, intervalo, h, condiciones_iniciales):
        try:
            y, t = sp.symbols('y t')
            intervalo = intervalo.split(',')
            condiciones_iniciales = condiciones_iniciales.split(',')

            a = float(intervalo[0])
            b = float(intervalo[1])
            h = float(h)

            co = np.array([float(condiciones_iniciales[0]), float(condiciones_iniciales[1])])

            def f(t, u):
                n = len(u)
                x1 = u[0]
                x2 = u[1]
                y = np.zeros(n)

                # Convertir las ecuaciones de texto a expresiones simbólicas
                ecuacion1 = sp.sympify(self.ecuaciones[0])
                ecuacion2 = sp.sympify(self.ecuaciones[1])

                # Crear funciones lambda utilizando lambdify
                f1 = sp.lambdify((t, x1, x2), ecuacion1, 'numpy')
                f2 = sp.lambdify((t, x1, x2), ecuacion2, 'numpy')

                # Calcular las derivadas
                y[0] = f1(t, x1, x2)
                y[1] = f2(t, x1, x2)

                return y

            yeu, t = ed.euler(f, a, b, h, co)
        except ValueError as e:
            tk.messagebox.showerror("Error", f"Error en los datos ingresados: {e}")
            return
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error inesperado: {e}")
            return

        self.ejes_ecuacion.clear()
        self.ejes_ecuacion.plot(t, yeu)
        self.canvas_ecuacion.draw()

    def uno_o_dos_euler(self, intervalo, h, condiciones_iniciales):
        try:
            self.ecuaciones.append(self.ecuacion1.get())
            self.ecuaciones.append(self.ecuacion2.get())

            if self.ecuaciones[1] == '':
                self.ejecutar_euler_primer_orden(self.ecuaciones[0], intervalo, h, condiciones_iniciales)
                self.ecuaciones.clear()
            else:
                self.ecuaciones_orden_superior_euler(intervalo, h, condiciones_iniciales)
                self.ecuaciones.clear()
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error inesperado: {e}")

    def uno_o_dos_runge(self, intervalo, h, condiciones_iniciales):
        try:
            self.ecuaciones.append(self.ecuacion1.get())
            self.ecuaciones.append(self.ecuacion2.get())

            if self.ecuaciones[1] == "":
                self.ejecutar_runge_kuta_primer_orden(self.ecuaciones[0], intervalo, h, condiciones_iniciales)
                self.ecuaciones.clear()
            else:
                # self.ecuaciones_orden_superior(intervalo, h, condiciones_iniciales)
                self.ecuaciones.clear()
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error inesperado: {e}")
