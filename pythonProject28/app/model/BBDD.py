import sqlite3
from tkinter import messagebox

class BBDD:
    def __init__(self, ruta):
        self.ruta = ruta
        self.miConexion = None
        self.miCursor = None
        self.connect()

    def connect(self):
        self.miConexion = sqlite3.connect(self.ruta)
        self.miConexion.execute("PRAGMA foreign_keys = ON")
        self.miConexion.commit()
        self.miCursor = self.miConexion.cursor()
        self.setUpDataBase()

    def setUpDataBase(self):
        self.miCursor.execute("""CREATE TABLE IF NOT EXISTS PRODUCTOS(
                                            ID INTEGER PRIMARY KEY AUTOINCREMENT,
                                            REFERENCIA VARCHAR(15) NOT NULL,
                                            CANTIDAD VARCHAR(5) NOT NULL,
                                            TURNO TEXT CHECK (TURNO IN ('T2C2','T2C1','T1C2','T1C1')) NOT NULL DEFAULT 'T2C2',
                                            FECHA DATE DEFAULT CURRENT_DATE
                                            )""")

        self.miConexion.commit()

        self.miCursor.execute("""CREATE TABLE IF NOT EXISTS UBICACION(
                                            ID INT PRIMARY KEY
                                            )""")
        self.miConexion.commit()

        try:
            self.miCursor.execute("""ALTER TABLE PRODUCTOS ADD COLUMN ID_UBICACION INTEGER NOT NULL REFERENCES UBICACION(ID);""")
            self.miConexion.commit
            self.miCursor.execute("""ALTER TABLE PRODUCTOS ADD COLUMN COMENTARIO  VARCHAR(100)""")
            self.miConexion.commit()
            self.miCursor.execute("""ALTER TABLE PRODUCTOS ADD COLUMN ID_DATE  VARCHAR(11)""")
            self.miConexion.commit()

            ubicaciones = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

            for u in ubicaciones:
                self.miCursor.execute("""INSERT INTO UBICACION (ID) VALUES(?)""", [u])
                self.miConexion.commit()
        except:
            pass

    def search_material(self, busqueda):
        self.miCursor.execute(f"""SELECT * FROM PRODUCTOS WHERE REFERENCIA LIKE '%{busqueda}%'""")
        self.miConexion.commit()
        data = self.miCursor.fetchall()
        return data

    def search_all_material(self):
        self.miCursor.execute("SELECT * FROM PRODUCTOS")
        self.miConexion.commit()
        data = self.miCursor.fetchall()
        return data

    def search_id(self, id):
        self.miCursor.execute(f"""SELECT * FROM PRODUCTOS WHERE ID = ?""", [id])
        self.miConexion.commit()
        data = self.miCursor.fetchall()
        return data[0]

    def search_by_id_material_and_reference(self,ref,id_date):
        self.miCursor.execute(f"""SELECT * FROM PRODUCTOS WHERE REFERENCIA = {ref} AND ID_DATE = {id_date}""")
        self.miConexion.commit()
        data = self.miCursor.fetchall()
        return data

    def insert(self, payload):

        self.miConexion.execute("PRAGMA foreign_keys = ON")
        self.miConexion.commit()

        try:
            self.miCursor.execute(f"""INSERT INTO PRODUCTOS (REFERENCIA, CANTIDAD, TURNO, ID_UBICACION, COMENTARIO, ID_DATE) VALUES(?,?,?,?,?,?)""",payload)
            self.miConexion.commit()

            self.miCursor.execute("SELECT MAX(ID) FROM PRODUCTOS")
            result = self.miCursor.fetchall()
            return result[0][0]

        except sqlite3.IntegrityError :
            messagebox.showerror("Error al crear", '''Kanban completo \n Vaciar antes de seguir insertando''')

    def count_registers(self, campo, tabla):
        self.miCursor.execute(f"SELECT COUNT({campo}) FROM {tabla}")
        count = self.miCursor.fetchall()
        return count[0][0]+1

    def count_material_id_ubi(self, id_ubi):
        self.miCursor.execute(f"SELECT COUNT(ID_UBICACION) FROM PRODUCTOS WHERE ID_UBICACION = {id_ubi}")
        count = self.miCursor.fetchall()
        return count[0][0]+1

    def delete(self, ref, id_date):

        self.miCursor.execute(f"""DELETE FROM PRODUCTOS WHERE REFERENCIA = {ref} AND ID_DATE = {id_date}""")
        self.miConexion.commit()

    def close(self):
        if self.miConexion:
            self.miConexion.commit()
            self.miCursor.close()
            self.miConexion.close()


