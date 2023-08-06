from tkinter import *
from tkinter.font import Font

ventana = Tk()
ventana.title("Crafting")
ventana.geometry("300x300")
ventana.configure(bg="grey")

etiqueta = Label(ventana, text = "Mesa de crafteo", bg="grey", font = ("MS Reference Sans Serif", 15))
etiqueta.pack()

caja = Entry(ventana)

caja.config()


ventana.mainloop()