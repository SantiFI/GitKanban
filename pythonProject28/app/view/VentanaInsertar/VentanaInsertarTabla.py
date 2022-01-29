from tkinter import Frame, Button, ttk, CENTER


class VentanaInsertarTabla(Frame):

    def __init__(self, master=None, width=None, height=None):
        #Creation and configuration of frame button contenedor for principal window

        super().__init__(master=master, width=width, height=height, bg="white")
        self.width = width
        self.height = height
        self.master = master
        self.place(x=0, y=110)
        self.create_widgets()

    def create_widgets(self):
        self.table_insertar = ttk.Treeview(self, columns=("col1", "col2", "col3", "col4", "col5", 'col6'),
                                               show='headings')
        self.table_insertar.column("col1", width=70, anchor=CENTER)
        self.table_insertar.column("col2", width=125, anchor=CENTER)
        self.table_insertar.column("col3", width=60, anchor=CENTER)
        self.table_insertar.column("col4", width=67, anchor=CENTER)
        self.table_insertar.column("col5", width=65, anchor=CENTER)
        self.table_insertar.column("col6", width=190, anchor=CENTER)
        self.table_insertar.heading("col1", text="ID", anchor=CENTER)
        self.table_insertar.heading("col2", text="Referencia", anchor=CENTER)
        self.table_insertar.heading("col3", text="Cantidad", anchor=CENTER)
        self.table_insertar.heading("col4", text="Turno", anchor=CENTER)
        self.table_insertar.heading("col5", text="Ubicacion", anchor=CENTER)
        self.table_insertar.heading("col6", text="Comentario", anchor=CENTER)
        self.table_insertar.grid(row=0, column=0, sticky='nsew')

        scrollbar = ttk.Scrollbar(self, command=self.table_insertar.yview)
        self.table_insertar.configure(yscroll=scrollbar.set)
        scrollbar.grid(row=0, column=1, sticky='nsew')
        self.boton_return = Button(self, text='Return', bg="SteelBlue3", font='Arial 11')
        self.boton_return.grid(row=1, column=0, columnspan=2, sticky='ew')