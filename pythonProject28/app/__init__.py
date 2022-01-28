from tkinter import Tk
from app.controller.VentanaInsertarController import VentanaInsertarController
from app.controller.VentanaPrincipalController import VentanaPrincipalController
from app.model.BBDD import BBDD

if __name__ == "__main__":

    db = BBDD(ruta="Kanban")
    ventana =VentanaPrincipalController(db)
    ventana.principal_window.mainloop()


