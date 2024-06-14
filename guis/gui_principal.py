import tkinter as tk
from tkinter import ttk
import guis.gui_taylor
import guis.gui_ed
import guis.gui_interpolacion
import guis.gui_ceros
import guis.gui_sde


class gui_principal:

    def __init__(self, root):
        self.root = root
        self.root.title("Análisis Numérico")
        self.root.geometry("500x300")
        self.root.resizable(False, False)


        # Paginas
        self.pagina_opciones = tk.Frame(self.root)

        # Inicializar las paginas
        self.inicializar_pagina_opciones()

        # Mostrar página principal
        self.mostrar_pagina(self.pagina_opciones)

    def inicializar_pagina_opciones(self):
        label = tk.Label(self.pagina_opciones, text="Menú principal")
        label.pack(pady=10)

        # Botones
        boton_taylor = tk.Button(self.pagina_opciones, text="Series de Taylor", width=50,
                                 command=self.abrir_pagina_taylor)
        boton_taylor.pack(pady=10)

        boton_ceros = tk.Button(self.pagina_opciones, text="Ceros de Funciones", width=50,
                                command=self.abrir_pagina_ceros)
        boton_ceros.pack(pady=10)

        boton_sistemas_ecuaciones = tk.Button(self.pagina_opciones, text="Sistemas de Ecuaciones Lineales", width=50,
                                              command=self.abrir_pagina_sistemas_ecuaciones)
        boton_sistemas_ecuaciones.pack(pady=10)

        boton_interpolacion = tk.Button(self.pagina_opciones, text="Interpolación y Ajuste Lineal", width=50,
                                        command=self.abrir_pagina_interpolacion)
        boton_interpolacion.pack(pady=10)

        boton_ecuaciones = tk.Button(self.pagina_opciones, text="Ecuaciones Diferenciales", width=50,
                                     command=self.abrir_pagina_ecuaciones)
        boton_ecuaciones.pack(pady=10)

    def abrir_pagina_taylor(self):
        guis.gui_taylor.PaginaTaylor(self.root)

    def abrir_pagina_ceros(self):
        guis.gui_ceros.PaginaCeros(self.root)
    def abrir_pagina_sistemas_ecuaciones(self):
        guis.gui_sde.PaginaSistemasEcuaciones(self.root)

    def abrir_pagina_interpolacion(self):
        guis.gui_interpolacion.PaginaInterpolacion(self.root)

    def abrir_pagina_ecuaciones(self):
        guis.gui_ed.PaginaEcuacionesDiferenciales(self.root)

    def mostrar_pagina(self, frame):
        frame.tkraise()
        frame.pack(fill='both', expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    gui = gui_principal(root)
    root.mainloop()
