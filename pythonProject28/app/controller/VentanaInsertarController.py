import tkinter
from datetime import datetime
from tkinter import Tk, messagebox
from tkinter.simpledialog import askstring

import app
from app.model.BBDD import BBDD
from app.view.VentanaInsertar.VentanaInsertarHead import VentanaInsertarHead
from app.view.VentanaInsertar.VentanaInsertarContent import VentanaInsertarContent
from app.view.VentanaInsertar.VentanaInsertarTabla import VentanaInsertarTabla


class VentanaInsertarController:
    def __init__(self, db: BBDD):
        self.principal_window = Tk()
        self.principal_window.wm_title("Kanban Automáticas")
        self.principal_window.resizable(False, False)
        self.principal_window.geometry("597x363+650+300")
        self.principal_window.grab_set()
        self.insertar_frame_head = VentanaInsertarHead(self.principal_window, 600, 50)
        self.insertar_frame_content = VentanaInsertarContent(self.principal_window, 600, 50)
        self.insertar_frame_tabla = VentanaInsertarTabla(self.principal_window, 600, 210)
        self.principal_window.iconbitmap('./resource/MM_ico.ico')
        self.db = db
        self.load_events()

    def load_events(self):
        self.insertar_frame_tabla.boton_return.configure(command=self.return_main)
        self.insertar_frame_content.campo_insertar.bind('<Return>', self.insertar_registro)

    def return_main(self):
        self.principal_window.destroy()
        app.VentanaPrincipalController(self.db)

    def insertar_registro(self, e):


        turno = self.calculate_shift()


        try:
            pre_payload = self.insertar_frame_content.campo_insertar.get()
            pre_payload = pre_payload.split("'")
            id_date = pre_payload[2]
            id_date = id_date.rstrip()
            pre_payload[2] = turno
            pre_payload.append(self.found_existent_material_ubicacion(payload=pre_payload))
            pre_payload.append(self.question_comment())
            pre_payload.append(id_date)
            print(pre_payload)
            last_id = self.db.insert(pre_payload)

            last_register = self.db.search_id(last_id)
            list_last_register = list(last_register)
            list_last_register.pop(4)
            self.insertar_frame_tabla.table_insertar.insert('', tkinter.END, values=list_last_register)
            self.insertar_frame_content.campo_insertar.delete(0, tkinter.END)
        except IndexError:
            messagebox.showerror("Error", "Datos insertados erroneos")


    def calculate_shift(self):
        # Generate shift automactly depending of now time
        now = datetime.now()
        week_day = datetime.today().isoweekday()
        if week_day == 7 or 1 <= week_day <= 3:
            if 18 >= now.hour <= 6:
                turno = "T2C2"
            else:
                turno = "T1C2"
        else:
            if 18 >= now.hour <= 6:
                turno = "T2C1"
            else:
                turno = "T1C1"
        return turno

    def found_existent_material_ubicacion(self, payload):
        data = self.db.search_material(payload[0])
        data_len = len(data)
        if not data:
            ubicacion_existent = self.found_ubication()
        else:
            for d in data:
                material_in_id = self.db.count_material_id_ubi(d[5])
                if material_in_id <= 10:
                    ubicacion_existent = d[5]
                else:
                    ubicacion_existent = self.found_ubication()



        return ubicacion_existent

    def question_comment(self):
        result = messagebox.askquestion("Comentario", "¿Quieres añadir un comentario?")

        if result == 'yes':
            name = askstring('Comentario', 'Añadir comentario al registro')
            return name
        else:
            return ''

    def found_ubication(self):
        ubications = self.db.count_registers("ID", "UBICACION")
        for i in range(ubications):
            i = i+1
            count_materiaul = self.db.count_material_id_ubi(i)
            if count_materiaul < 10:
                ubicacion_re = i
                return ubicacion_re
            else:
                pass


