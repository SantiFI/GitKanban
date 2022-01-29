import tkinter.font
from tkinter import Tk, Frame, PhotoImage, Button

class VentanaPrincipalContent(Frame):

    def __init__(self, master=None, width=None, height=None):
        #Creation and configuration of frame button contenedor for principal window

        super().__init__(master=master, width=width, height=height, bg="white")
        self.width = width
        self.height = height
        self.master = master
        self.place(x=0, y=50)
        self.create_widgets()

    def create_widgets(self):
        # Creation of buttoms
        self.boton_insertar = Button(master=self, text='Insertar nuevo registro', width=25, height=2, font=tkinter.font.Font(size=13))
        self.boton_insertar.place(x=35, y=5)

        self.boton_buscar = Button(master=self, text='Buscar registro', width=25, height=2,font=tkinter.font.Font(size=13))
        self.boton_buscar.place(x=35, y=65)

        self.boton_listar = Button(master=self, text='Listar todos los registros', width=25, height=2, font=tkinter.font.Font(size=13))
        self.boton_listar.place(x=35, y=125)

        self.boton_eliminar = Button(master=self, text='Eliminar registros', width=25, height=2, font=tkinter.font.Font(size=13))
        self.boton_eliminar.place(x=35, y=185)

        self.boton_salir = Button(master=self, text='Salir', width=25, height=2, font=tkinter.font.Font(size=13))
        self.boton_salir.place(x=35, y=245)