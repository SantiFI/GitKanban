from tkinter import Tk

import app
from app.model.BBDD import BBDD
from app.view.VentanaPrincipal.VentanaPrincipalContent import VentanaPrincipalContent
from app.view.VentanaPrincipal.VentanaPrincipalHead import VentanaPrincipalHead


class VentanaPrincipalController:
    def __init__(self, db:BBDD):
        self.principal_window = Tk()
        self.principal_window.wm_title("Kanban Automáticas")
        self.principal_window.resizable(False, False)
        self.principal_window.geometry("300x350+800+300")
        self.principal_frame_head = VentanaPrincipalHead(self.principal_window, 300, 50)
        self.principal_frame_content = VentanaPrincipalContent(self.principal_window, 300, 300)
        self.principal_window.iconbitmap('./resource/MM_ico.ico')
        self.db = db
        self.load_events()

    def load_events(self):
        self.principal_window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.principal_frame_content.boton_salir.configure(command= lambda :self.on_closing())
        self.principal_frame_content.boton_insertar.configure(command=  self.change_to_insertar)
        self.principal_frame_content.boton_buscar.configure(command=self.change_to_buscar)

    def change_to_insertar(self):
        self.principal_window.destroy()
        app.VentanaInsertarController(self.db)

    def change_to_buscar(self):
        self.principal_window.destroy()
        app.VentanaBuscarController(self.db)

    def on_closing(self):
        self.db.close()
        self.principal_window.destroy()


