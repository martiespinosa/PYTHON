from tkinter import *
from tkinter.ttk import *
from customtkinter import *

root = Tk()
app = CTkFrame(root)
app.pack(fill = BOTH, expand = 1)



solo_numeros1 =  lambda text: text.isdecimal()
solo_uno1 = StringVar()
solo_numeros2 =  lambda text: text.isdecimal()
solo_uno2 = StringVar()
solo_numeros3 =  lambda text: text.isdecimal()
solo_uno3 = StringVar()
solo_numeros4 =  lambda text: text.isdecimal()
solo_uno4 = StringVar()
solo_numeros5 =  lambda text: text.isdecimal()
solo_uno5 = StringVar()
solo_numeros6 =  lambda text: text.isdecimal()
solo_uno6 = StringVar()

uno = CTkEntry(master = app, width = 23, height =20, font=("Dubai", 10, "bold"), validate="key", validatecommand=(app.register(solo_numeros1), "%S"), textvariable=solo_uno1)
uno.place(relx=0.1, rely=0.1)

dos = CTkEntry(master = app, width = 23, height =20, font=("Dubai", 10, "bold"), validate="key", validatecommand=(app.register(solo_numeros2), "%S"), textvariable=solo_uno2)
dos.place(relx=0.25, rely=0.1)

tres = CTkEntry(master = app, width = 23, height =20, font=("Dubai", 10, "bold"), validate="key", validatecommand=(app.register(solo_numeros3), "%S"), textvariable=solo_uno3)
tres.place(relx=0.4, rely=0.1)

cuatro = CTkEntry(master = app, width = 23, height =20, font=("Dubai", 10, "bold"), validate="key", validatecommand=(app.register(solo_numeros4), "%S"), textvariable=solo_uno4)
cuatro.place(relx=0.55, rely=0.1)

cinco = CTkEntry(master = app, width = 23, height =20, font=("Dubai", 10, "bold"), validate="key", validatecommand=(app.register(solo_numeros5), "%S"), textvariable=solo_uno5)
cinco.place(relx=0.7, rely=0.1)

seis = CTkEntry(master = app, width = 23, height =20, font=("Dubai", 10, "bold"), validate="key", validatecommand=(app.register(solo_numeros6), "%S"), textvariable=solo_uno6)
seis.place(relx=0.85, rely=0.1)

prueba = CTkEntry(app)
prueba.place(relx=0.5, rely=0.5, anchor = CENTER)




def limitador(solo_uno1):
    if len(solo_uno1.get()) > 1:
        solo_uno1.set(solo_uno1.get()[:1])
solo_uno1.trace("w", lambda *args: limitador(solo_uno1))

def limitador(solo_uno2):
    if len(solo_uno2.get()) > 1:
        solo_uno2.set(solo_uno2.get()[:1])
solo_uno2.trace("w", lambda *args: limitador(solo_uno2))

def limitador(solo_uno3):
    if len(solo_uno3.get()) > 1:
        solo_uno3.set(solo_uno3.get()[:1])
solo_uno3.trace("w", lambda *args: limitador(solo_uno3))

def limitador(solo_uno4):
    if len(solo_uno4.get()) > 1:
        solo_uno4.set(solo_uno4.get()[:1])
solo_uno4.trace("w", lambda *args: limitador(solo_uno4))

def limitador(solo_uno5):
    if len(solo_uno5.get()) > 1:
        solo_uno5.set(solo_uno5.get()[:1])
solo_uno5.trace("w", lambda *args: limitador(solo_uno5))

def limitador(solo_uno5):
    if len(solo_uno5.get()) > 1:
        solo_uno5.set(solo_uno5.get()[:1])
solo_uno5.trace("w", lambda *args: limitador(solo_uno5))


www = True
while www == True:
    if uno.get() == "":
        uno.focus_set()
    elif uno.get() != "" and dos.get() == "":
        uno.focus_set()
        dos.focus_set()
    elif uno.get()!= "" and dos.get()!= "" and tres.get() == "":
        tres.focus_set()
    elif uno.get()!= "" and dos.get()!= "" and tres.get()!= "" and cuatro.get() == "":
        cuatro.focus_set()
    elif uno.get()!= "" and dos.get()!= "" and tres.get()!= "" and cuatro.get() != "" and cinco.get() == "":
        cinco.focus_set()
    elif uno.get()!= "" and dos.get()!= "" and tres.get()!= "" and cuatro.get()!= "" and cinco.get()!= "" and seis.get() == "":
        seis.focus_set()
        www = False




root.mainloop()