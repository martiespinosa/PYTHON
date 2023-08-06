from tkinter import *

raiz = Tk()


varSexo = IntVar()

def sexo():


    if varSexo.get() == 1:
        textoFinal1.config(text="Eres hombre")

    if varSexo.get() == 2:
        textoFinal1.config(text="Eres mujer")

    if varSexo.get() == 3:
        textoFinal1.config(text="Eres ""otros""")





varA = IntVar()
varE = IntVar()
varI = IntVar()
varO = IntVar()
varU = IntVar()

def vocales():
    varVocales = ""

    if varA.get() == 1:
        varVocales += " A"

    if varE.get() == 1:
        varVocales += " E"

    if varI.get() == 1:
        varVocales += " I"

    if varO.get() == 1:
        varVocales += " O"

    if varU.get() == 1:
        varVocales += " U"

    textoFinal2.config(text="Tu mobre tiene estas vocales:" + varVocales)        


frame = Frame(raiz, bg="beige", width=200, height=200)
frame.pack(fill="both", expand=1)

foto = PhotoImage(file=r"C:\Users\MARTI\Desktop\PYTHON\INTERFACES GRÁFICAS\muñecoRojo.png")

Label(frame, image=foto, bg="beige").pack()

Label(frame, text="Selecciona tu sexo:", bg="beige").pack()

Radiobutton(frame, text="Hombre", bg="beige", variable=varSexo, value=1, command=sexo).pack()
Radiobutton(frame, text="Mujer", bg="beige", variable=varSexo, value=2, command=sexo).pack()
Radiobutton(frame, text="Otros", bg="beige", variable=varSexo, value=3, command=sexo).pack()

Label(frame, text="", bg="beige").pack()

Label(frame, text="Indica las vocales que estén en tu nombre:", bg="beige").pack()

a = Checkbutton(frame, text="A", bg="beige", variable=varA, onvalue=1, offvalue=0, command=vocales).pack()
e = Checkbutton(frame, text="E", bg="beige", variable=varE, onvalue=1, offvalue=0, command=vocales).pack()
i = Checkbutton(frame, text="I", bg="beige", variable=varI, onvalue=1, offvalue=0, command=vocales).pack()
o = Checkbutton(frame, text="O", bg="beige", variable=varO, onvalue=1, offvalue=0, command=vocales).pack()
u = Checkbutton(frame, text="U", bg="beige", variable=varU, onvalue=1, offvalue=0, command=vocales).pack()

Label(frame, text="", bg="beige").pack()

textoFinal1 = Label(frame, bg="beige", fg="red")
textoFinal1.pack()

textoFinal2 = Label(frame, bg="beige", fg="red")
textoFinal2.pack()

raiz.mainloop()