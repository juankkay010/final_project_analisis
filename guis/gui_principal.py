import tkinter as tk
import guis.gui_taylor as ty

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
        ty.PaginaTaylor(self.root)


    def abrir_pagina_ceros(self):
        pagina = tk.Toplevel(self.root)
        pagina.title("Ceros de funciones")
        pagina.geometry("500x500")

        label = tk.Label(pagina, text="Ceros de funciones")
        label.pack(pady=10)

    def abrir_pagina_sistemas_ecuaciones(self):
        pagina = tk.Toplevel(self.root)
        pagina.title("Sistemas de Ecuaciones Lineales")
        pagina.geometry("500x500")
        label = tk.Label(pagina, text="Sistemas de Ecuaciones")
        label.pack(pady=10)

    def abrir_pagina_interpolacion(self):
        pagina = tk.Toplevel(self.root)
        pagina.title("Interpolacion y Ajuste Lineal")
        pagina.geometry("500x500")

        label = tk.Label(pagina, text="Interpolacion y Ajuste Lineal")
        label.pack(pady=10)

    def abrir_pagina_ecuaciones(self):
        pagina = tk.Toplevel(self.root)
        pagina.title("Ecuaciones Diferenciales")
        pagina.geometry("500x500")
        label = tk.Label(pagina, text="Ecuaciones Diferenciales")
        label.pack(pady=10)

    def mostrar_pagina(self, frame):
        frame.tkraise()
        frame.pack(fill='both', expand=True)


if __name__ == "__main__":
    root = tk.Tk()
    gui = gui_principal(root)
    root.mainloop()
