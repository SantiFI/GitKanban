import tkinter
from tkinter import Tk, messagebox

import app
from app.model.BBDD import BBDD
from app.view.VentanaBucar.VentanaBuscarHead import VentanaBuscarHead
from app.view.VentanaBucar.VentanaBuscarContent import VentanaBuscarContent
from app.view.VentanaBucar.VentanaBuscarTable import VentanaBuscarTabla


class VentanaBuscarController:
    def __init__(self, db: BBDD):
        self.principal_window = Tk()
        self.principal_window.wm_title("Kanban Automáticas")
        self.principal_window.resizable(False, False)
        self.principal_window.geometry("600x395+650+300")
        self.principal_window.grab_set()
        self.buscar_frame_head = VentanaBuscarHead(self.principal_window, 600, 50)
        self.buscar_frame_content = VentanaBuscarContent(self.principal_window, 600, 50)
        self.buscar_frame_tabla = VentanaBuscarTabla(self.principal_window, 600, 250)
        self.principal_window.iconbitmap('./resource/MM_ico.ico')
        self.db = db
        self.load_events()

    def load_events(self):
        self.buscar_frame_tabla.boton_return.configure(command=self.return_main)
        self.buscar_frame_content.campo_buscar.bind('<Return>', self.buscar_registro)
        self.buscar_frame_tabla.boton_buscar.configure(command=self.buscar_registro_boton)

    def buscar_registro(self, e):

        try:

            for item in self.buscar_frame_tabla.table_buscar.get_children():
                self.buscar_frame_tabla.table_buscar.delete(item)

            busqueda = self.buscar_frame_content.campo_buscar.get()
            busqueda = busqueda.split("'")
            ref = busqueda[0]
            data = self.db.search_material(ref)

            res = [list(ele) for ele in data]

            for r in res:
                r[4] = r[5]
                r[5] = r[6]

            for l in res:
                self.buscar_frame_tabla.table_buscar.insert('', tkinter.END, values=l)

            self.buscar_frame_content.campo_buscar.delete(0, tkinter.END)
        except IndexError:
            messagebox.showerror("Error", "Datos insertados erroneos")

    def buscar_registro_boton(self):
        try:

            for item in self.buscar_frame_tabla.table_buscar.get_children():
                self.buscar_frame_tabla.table_buscar.delete(item)

            busqueda = self.buscar_frame_content.campo_buscar.get()
            busqueda = busqueda.split("'")
            ref = busqueda[0]
            data = self.db.search_material(ref)

            res = [list(ele) for ele in data]

            for r in res:
                r[4] = r[5]
                r[5] = r[6]

            for l in res:
                self.buscar_frame_tabla.table_buscar.insert('', tkinter.END, values=l)
            self.buscar_frame_content.campo_buscar.delete(0, tkinter.END)
        except IndexError:
            messagebox.showerror("Error", "Datos insertados erroneos")

    def return_main(self):
        self.principal_window.destroy()
        app.VentanaPrincipalController(self.db)
