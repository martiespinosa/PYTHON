from tkinter import *
from tkinter.font import Font

raiz = Tk()
raiz.title("Calculadora")

raiz.configure(bg="black")

#entrada de texto
entradaTexto = Entry(raiz, font = ("MS Reference Sans Serif",), border="0", justify="right")
entradaTexto.grid(row = 0, column = 0, columnspan=4, rowspan=1)
entradaTexto.configure(bg = "black")
entradaTexto.configure(fg = "white")

#creación de botones
boton1 = Button(raiz, text = "1", width=5, height=2, border="0", bg="grey", fg="white")
boton2 = Button(raiz, text = "2", width=5, height=2, border="0", bg="grey", fg="white")
boton3 = Button(raiz, text = "3", width=5, height=2, border="0", bg="grey", fg="white")
boton4 = Button(raiz, text = "4", width=5, height=2, border="0", bg="grey", fg="white")
boton5 = Button(raiz, text = "5", width=5, height=2, border="0", bg="grey", fg="white")
boton6 = Button(raiz, text = "6", width=5, height=2, border="0", bg="grey", fg="white")
boton6 = Button(raiz, text = "6", width=5, height=2, border="0", bg="grey", fg="white")
boton7 = Button(raiz, text = "7", width=5, height=2, border="0", bg="grey", fg="white")
boton8 = Button(raiz, text = "8", width=5, height=2, border="0", bg="grey", fg="white")
boton9 = Button(raiz, text = "9", width=5, height=2, border="0", bg="grey", fg="white")
boton0 = Button(raiz, text = "0", width=15, height=2, border="0", bg="grey", fg="white")
botonComa = Button(raiz, text = ",", width=5, height=2, border="0", bg="grey", fg="white")

botonSuma = Button(raiz, text = "+", width=5, height=2, border="0", bg="orange", fg="white")
botonResta = Button(raiz, text = "-", width=5, height=2, border="0", bg="orange", fg="white")
botonMulti = Button(raiz, text = "×", width=5, height=2, border="0", bg="orange", fg="white")
botonDivi = Button(raiz, text = "÷", width=5, height=2, border="0", bg="orange", fg="white")
botonIgual = Button(raiz, text = "=", width=5, height=2, border="0", bg="orange", fg="white")

botonBorrar = Button(raiz, text = "AC", width=5, height=2, border="0", bg="dark gray", fg="black")
botonSigno = Button(raiz, text = "±", width=5, height=2, border="0", bg="dark gray", fg="black")
botonPorce = Button(raiz, text = "%", width=5, height=2, border="0", bg="dark gray", fg="black")


#agregar los botones en patalla
boton1.grid(row=4, column=0)
boton2.grid(row=4, column=1)
boton3.grid(row=4, column=2)
boton4.grid(row=3, column=0)
boton5.grid(row=3, column=1)
boton6.grid(row=3, column=2)
boton7.grid(row=2, column=0)
boton8.grid(row=2, column=1)
boton9.grid(row=2, column=2)
boton0.grid(row=5, column=0, columnspan=2)
botonComa.grid(row=5, column=2)

botonSuma.grid(row=4, column=3)
botonResta.grid(row=3, column=3)
botonMulti.grid(row=2, column=3)
botonDivi.grid(row=1, column=3)
botonIgual.grid(row=5, column=3)

botonBorrar.grid(row=1, column=0)
botonSigno.grid(row=1, column=1)

botonPorce.grid(row=1, column=2)

raiz.mainloop()
    