from tkinter import *

raiz = Tk()
raiz.title("Texto de ejemplo")
# raiz.geometry("650x350") #al darle tamaño al contenedor no se le tiene que dar a la raiz, ya que se adapta al tamaño del contenedor
raiz.config(bg = "navajowhite4")

contenedor = Frame()
contenedor.pack(fill = "both", expand = "y")
# contenedor.pack(side = "bottom", anchor = "e")
contenedor.config(bg = "pink")
contenedor.config(width = "550", height = "330")
contenedor.config(cursor = "hand2")

etiqueta = Label(contenedor, text = "Texto de ejemplo", bg = "pink", fg = "saddlebrown", font = ("MS Reference Sans Serif", 90))
etiqueta.place(x = 100, y = 100)

projo = PhotoImage(file = r"C:\Users\MARTI\Desktop\PYTHON\INTERFACES GRÁFICAS\muñecoRojo.png")
Label(contenedor, image = projo, bg = "pink").place(x = 470, y = 250)


raiz.mainloop()