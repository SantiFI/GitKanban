from tkinter import  Frame,  Entry, SUNKEN


class VentanaBuscarContent(Frame):

    def __init__(self, master=None, width=None, height=None):
        #Creation and configuration of frame button contenedor for principal window

        super().__init__(master=master, width=width, height=height, bg="white")
        self.width = width
        self.height = height
        self.master = master
        self.place(x=0, y=50)
        self.create_widgets()

    def create_widgets(self):
        self.campo_buscar = Entry(self, width=30, font='Arial 24', relief=SUNKEN, bg='white smoke')
        self.campo_buscar.focus_force()
        self.campo_buscar.grid(column = 0, sticky = 'nsew', padx=30, pady=10)