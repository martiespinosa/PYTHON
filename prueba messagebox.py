from tkinter import *
from tkinter import messagebox

root = Tk()
root.config(bg="blue")

def info():
    messagebox.showinfo("Información sobre el programa", "Este es un programa de prueba para practicar los messageboxes de tkinter")

def advertencia():
    messagebox.showwarning("Advertencia", "Este es un mensaje de advertencia de prueba")

def preguntaSiNo():
    messagebox.askyesno("Pregunta", "Te gusta este pregrama?")

def preguntaOKCancel():
    messagebox.askyesnocancel("Pregunta", "Prueba")

boton1 = Button(root, text="Info", command=info)
boton1.pack()

boton2 = Button(root, text="Advertencia", command=advertencia)
boton2.pack()

boton3 = Button(root, text="Pregunta Si o No", command=preguntaSiNo)
boton3.pack()

boton3 = Button(root, text="Pregunta OK Cancel", command=preguntaOKCancel)
boton3.pack()


root.mainloop()
