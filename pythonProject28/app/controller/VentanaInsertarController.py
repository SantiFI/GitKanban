from tkinter import Tk

import app
from app.view.VentanaInsertar.VentanaInsertarHead import VentanaInsertarHead
from app.view.VentanaInsertar.VentanaInsertarContent import VentanaInsertarContent
from app.view.VentanaInsertar.VentanaInsertarTabla import VentanaInsertarTabla


class VentanaInsertarController:
    def __init__(self):
        self.principal_window = Tk()
        self.principal_window.wm_title("Kanban Automáticas")
        self.principal_window.resizable(False, False)
        self.principal_window.geometry("597x363+650+300")
        self.principal_window.grab_set()
        self.insertar_frame_head = VentanaInsertarHead(self.principal_window, 600, 50)
        self.insertar_frame_content = VentanaInsertarContent(self.principal_window, 600, 50)
        self.insertar_frame_tabla = VentanaInsertarTabla(self.principal_window, 600, 210)
        self.principal_window.iconbitmap('./resource/MM_ico.ico')
        self.load_events()

    def load_events(self):
        self.insertar_frame_tabla.boton_return.configure(command= self.return_main)
        self.insertar_frame_content.campo_insertar.bind('<Return>', self.insertar_registro)

    def return_main(self):
        self.principal_window.destroy()
        app.VentanaPrincipalController()

    def insertar_registro(self, e):
            print('Enter pulado')

