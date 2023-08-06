from tkinter import *

raiz = Tk()


def click():
    salidaTexto = entradaTexto.get()

    salidaTexto = salidaTexto.replace("a", "1")
    salidaTexto = salidaTexto.replace("e", "2")
    salidaTexto = salidaTexto.replace("i", "3")
    salidaTexto = salidaTexto.replace("o", "4")
    salidaTexto = salidaTexto.replace("u", "5")
    salidaTexto = salidaTexto.replace("A", "1")
    salidaTexto = salidaTexto.replace("E", "2")
    salidaTexto = salidaTexto.replace("I", "3")
    salidaTexto = salidaTexto.replace("O", "4")
    salidaTexto = salidaTexto.replace("U", "5")
           
    final.config(text=salidaTexto)


frame = Frame(bg="purple1", width=800, height=500)
frame.pack(fill="both", expand=1)

Label(frame, bg="purple1", text="\nCONVERTIR VOCALES EN NÚMEROS\n\nA = 1\nE = 2\nI = 3\nO = 4\nU = 5\n", font=(50)).pack()

entradaTexto = Entry(frame)
entradaTexto.pack()

Label(frame, bg="purple1", text="").pack()

boton = Button(frame, text="Convertir", command=click)
boton.pack()

final = Label(frame, bg="purple1")
final.pack()

raiz.mainloop()


