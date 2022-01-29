import tkinter
from tkinter import Tk, messagebox

import app
from app.model.BBDD import BBDD
from app.view.VentanaListar.VentanaListarHead import VentanaListarHead
from app.view.VentanaListar.VentanaListarTabla import VentanaListarTabla


class VentanaListarController:
    def __init__(self, db: BBDD):
        self.principal_window = Tk()
        self.principal_window.wm_title("Kanban Automáticas")
        self.principal_window.resizable(False, False)
        self.principal_window.geometry("600x300+650+300")
        self.principal_window.grab_set()
        self.listar_frame_head = VentanaListarHead(self.principal_window, 600, 50)
        self.listar_frame_tabla = VentanaListarTabla(self.principal_window, 600, 250)
        self.principal_window.iconbitmap('./resource/MM_ico.ico')
        self.db = db
        self.load_events()

    def load_events(self):
        self.listar_frame_tabla.boton_return.configure(command=self.return_main)
        self.listar_registro()

    def listar_registro(self):

        try:

            for item in self.listar_frame_tabla.table_Listar.get_children():
                self.listar_frame_tabla.table_Listar.delete(item)

            data = self.db.search_all_material()

            res = [list(ele) for ele in data]

            for r in res:
                r[4] = r[5]
                r[5] = r[6]

            for l in res:
                self.listar_frame_tabla.table_Listar.insert('', tkinter.END, values=l)

        except IndexError:
            messagebox.showerror("Error", "Datos insertados erroneos")


    def return_main(self):
        self.principal_window.destroy()
        app.VentanaPrincipalController(self.db)