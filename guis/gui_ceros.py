import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sympy as sp
import numpy as np
from functions import ceros

class PaginaCeros(tk.Toplevel):
    def __init__(self, root):
        super().__init__(root)
        self.geometry("1366x768")
        self.configure(bg="#ADD8E6")
        self.x = sp.symbols('x')
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

        label_intervalo = ttk.Label(self, text="Ingrese el intervalo o el punto inicial:")
        label_intervalo.grid(row=1, column=0, padx=10, pady=10, sticky="e")
        self.intervalo = ttk.Entry(self, width=100)
        self.intervalo.grid(row=1, column=1, padx=10, pady=10, sticky="w")

        label_tol = ttk.Label(self, text="Ingrese la tolerancia:")
        label_tol.grid(row=2, column=0, padx=10, pady=10, sticky="e")
        self.tol = ttk.Entry(self, width=100)
        self.tol.grid(row=2, column=1, padx=10, pady=10, sticky="w")

        boton_biseccion = ttk.Button(self, text="Método de Bisección", command=self.ejecutar_biseccion)
        boton_biseccion.grid(row=3, column=0, padx=10, pady=10, sticky="e")

        boton_newton = ttk.Button(self, text="Método de Newton", command=self.ejecutar_newton)
        boton_newton.grid(row=3, column=1, padx=10, pady=10, sticky="w")

        boton_falsa_pos = ttk.Button(self, text="Método de la Falsa Posición", command=self.ejecutar_falsa_posicion)
        boton_falsa_pos.grid(row=3, column=2, padx=10, pady=10, sticky="e")

        boton_secante = ttk.Button(self, text="Método de la Secante", command=self.ejecutar_secante)
        boton_secante.grid(row=3, column=3, padx=10, pady=10, sticky="e")

        label_resultado = ttk.Label(self, text="Resultado:")
        label_resultado.grid(row=4, column=0, padx=10, pady=10, sticky="e")
        self.resultado = tk.Text(self, height=5, width=50)
        self.resultado.grid(row=4, column=1, padx=10, pady=10, sticky="e")

    def ejecutar_biseccion(self):
        try:
            funcion = sp.sympify(self.funcion.get())
            lambd = sp.lambdify(self.x, funcion)
            intervalo = self.intervalo.get().split(",")
            a = float(intervalo[0])
            b = float(intervalo[1])
            tol = float(self.tol.get())
            resultado = ceros.biseccion(lambd, a, b, tol)
        except (ValueError, IndexError) as e:
            tk.messagebox.showerror("Error", f"Error en los datos ingresados: {e}")
            return
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error inesperado: {e}")
            return

        self.resultado.delete('1.0', tk.END)
        self.resultado.insert(tk.END, resultado)

    def ejecutar_newton(self):
        try:
            funcion = sp.sympify(self.funcion.get())
            punto_inicial = float(self.intervalo.get())
            tol = float(self.tol.get())
            resultado = ceros.newton(funcion, punto_inicial, tol)
        except (ValueError, IndexError) as e:
            tk.messagebox.showerror("Error", f"Error en los datos ingresados: {e}")
            return
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error inesperado: {e}")
            return

        self.resultado.delete('1.0', tk.END)
        self.resultado.insert(tk.END, resultado)

    def ejecutar_falsa_posicion(self):
        try:
            funcion = sp.sympify(self.funcion.get())
            lambd = sp.lambdify(self.x, funcion)
            intervalo = self.intervalo.get().split(",")
            a = float(intervalo[0])
            b = float(intervalo[1])
            tol = float(self.tol.get())
            resultado = ceros.posicion_falsa(lambd, a, b, tol)
        except (ValueError, IndexError) as e:
            tk.messagebox.showerror("Error", f"Error en los datos ingresados: {e}")
            return
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error inesperado: {e}")
            return

        self.resultado.delete('1.0', tk.END)
        self.resultado.insert(tk.END, resultado)

    def ejecutar_secante(self):
        try:
            funcion = sp.sympify(self.funcion.get())
            lambd = sp.lambdify(self.x, funcion)
            intervalo = self.intervalo.get().split(",")
            a = float(intervalo[0])
            b = float(intervalo[1])
            tol = float(self.tol.get())
            resultado = ceros.secante(lambd, a, b, tol)
        except (ValueError, IndexError) as e:
            tk.messagebox.showerror("Error", f"Error en los datos ingresados: {e}")
            return
        except Exception as e:
            tk.messagebox.showerror("Error", f"Error inesperado: {e}")
            return

        self.resultado.delete('1.0', tk.END)
        self.resultado.insert(tk.END, resultado)