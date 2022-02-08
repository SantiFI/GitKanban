import tkinter
from datetime import datetime
from tkinter import Tk, messagebox
from tkinter.simpledialog import askstring

import app
from app.model.BBDD import BBDD
from app.view.VentanaEliminar.VentanaEliminarHead import VentanaEliminarHead
from app.view.VentanaEliminar.VentanaEliminarContent import VentanaEliminarContent
from app.view.VentanaEliminar.VentanaEliminatTabla import VentanaEliminarTabla


class VentanaEliminarController:
    def __init__(self, db: BBDD):
        self.principal_window = Tk()
        self.principal_window.wm_title("Kanban Automáticas")
        self.principal_window.resizable(False, False)
        self.principal_window.geometry("600x395+650+300")
        self.principal_window.grab_set()
        self.eliminar_frame_head = VentanaEliminarHead(self.principal_window, 600, 50)
        self.eliminar_frame_content = VentanaEliminarContent(self.principal_window, 600, 50)
        self.eliminar_frame_tabla = VentanaEliminarTabla(self.principal_window, 600, 210)
        self.principal_window.iconbitmap('./resource/MM_ico.ico')
        self.db = db
        self.load_events()

    def load_events(self):
        self.eliminar_frame_tabla.boton_return.configure(command=self.return_main)
        self.eliminar_frame_content.campo_eliminar.bind('<Return>', self.eliminar_registro)
        self.eliminar_frame_tabla.boton_buscar.configure(command=self.eliminar_registro_boton)

    def return_main(self):
        self.principal_window.destroy()
        app.VentanaPrincipalController(self.db)

    def eliminar_registro(self, e):

        try:
            pre_payload = self.eliminar_frame_content.campo_eliminar.get()
            pre_payload = pre_payload.split("'")
            id_date = pre_payload[2]
            id_date = id_date.rstrip()
            ref = pre_payload[0]
            ref = ref.split(".")
            ref = ref[0]
            registro = self.db.search_by_id_material_and_reference(ref,id_date)

            if not registro:
                messagebox.showerror("Error", "Registro no en Kanban")
                self.eliminar_frame_content.campo_eliminar.delete(0, tkinter.END)

            self.db.delete(ref, id_date)
            registro = list(registro)
            for r in registro:
                r = list(r)
                r.pop(4)
                self.eliminar_frame_tabla.table_eliminar.insert('', tkinter.END, values=r)
                self.eliminar_frame_content.campo_eliminar.delete(0, tkinter.END)
        except IndexError:
            messagebox.showerror("Error", "Datos insertados erroneos")

    def eliminar_registro_boton(self):

        try:
            pre_payload = self.eliminar_frame_content.campo_eliminar.get()
            pre_payload = pre_payload.split("'")
            id_date = pre_payload[2]
            id_date = id_date.rstrip()
            ref = pre_payload[0]
            registro = self.db.search_by_id_material_and_reference(ref,id_date)

            if not registro:
                messagebox.showerror("Error", "Registro no en Kanban")
                self.eliminar_frame_content.campo_eliminar.delete(0, tkinter.END)

            self.db.delete(ref, id_date)
            registro = list(registro)
            for r in registro:
                r = list(r)
                r.pop(4)
                self.eliminar_frame_tabla.table_eliminar.insert('', tkinter.END, values=r)
                self.eliminar_frame_content.campo_eliminar.delete(0, tkinter.END)
        except IndexError:
            messagebox.showerror("Error", "Datos insertados erroneos")