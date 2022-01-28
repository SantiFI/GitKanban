import tkinter
from tkinter import Tk, Frame, PhotoImage, Label, font


class VentanaPrincipalHead(Frame):

    def __init__(self, master=None, width=None, height=None):
        super().__init__(master, width=width, height=height, bg="SteelBlue3")
        self.width = width
        self.height = height
        self.master = master
        self.pack()
        self.marelli_img = PhotoImage(file='./resource/MM.png')
        self.Lighting_img = PhotoImage(file='./resource/AL.png')
        self.create_widgets()

    def create_widgets(self):
        # Creation of PhotoImage to put inside of labtel to show images


        #Creation of labels
        label_img_MM = Label(self, image=self.marelli_img)
        label_img_MM.place(x=5, y=3)
        label_img_AL = Label(self, image=self.Lighting_img)
        label_img_AL.place(x=230, y=22)
        label_superior = Label(self, text='KANBAN \n AUTOMÁTICAS', bg='SteelBlue3', font=tkinter.font.Font(family="Lucia Grande bold", size=12))
        label_superior.place(x=85, y=5)
