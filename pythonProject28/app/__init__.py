from tkinter import Tk
from app.controller.VentanaInsertarController import VentanaInsertarController
from app.controller.VentanaPrincipalController import VentanaPrincipalController


if __name__ == "__main__":

    ventana =VentanaPrincipalController()
    ventana.principal_window.mainloop()


