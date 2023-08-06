# COSAS A MEJORAR:
# 1. Al escribir todo el codigo no deja borrar
# 2. Si el usuario selecciona el último entry cuando ya tiene un nuemro, deja escribir mas de un numero por entry

from tkinter import *
from tkinter.ttk import *
from customtkinter import *

root = CTk()
root.geometry("250x250")
app = CTkFrame(root)
app.pack(fill=BOTH, expand=1)

solo_numeros = lambda text: text.isdecimal()
solo_uno1 = StringVar()
solo_uno2 = StringVar()
solo_uno3 = StringVar()
solo_uno4 = StringVar()
solo_uno5 = StringVar()
solo_uno6 = StringVar()


def validar_y_mover(event, entry_actual, entry_siguiente):
    if  entry_actual != boton and entry_siguiente != boton and entry_actual.get() == "":
        entry_actual.focus_set()
    elif entry_actual != boton and entry_siguiente != boton and entry_actual.get() != "" and entry_siguiente.get() == "":
        entry_siguiente.focus_set()
        entry_siguiente = entry_actual
    elif entry_actual == boton:
        boton.focus_set()
        return False

    if solo_numeros(event):
        entry_siguiente.focus_set()
        return solo_numeros(event)
    return False


# def validar_y_mover_ultimate(event, entry_actual, boton):

#     boton.focus_set()
        
#     if solo_numeros(event) and len(seis.get()) < 1:
#         boton.focus_set()
#         return solo_numeros(event)
#     return False



# def validar_solo_numeros(char):
#     return char.isdigit() and len(seis.get()) < 1


def borrar_y_mover(event, entry_actual, entry_anterior):
    if entry_actual != boton and event.keysym == "BackSpace" and len(entry_actual.get()) == 0:
        entry_anterior.focus_set()
        entry_anterior.delete(0, END)
    elif entry_actual != boton and event.keysym == "BackSpace" and len(entry_actual.get()) != 0:
        entry_actual.focus_set()
        entry_actual.delete(0, END)
    elif entry_actual == boton and event.keysym == "BackSpace":
        entry_anterior.delete(0, END)
        entry_anterior.focus_set()




uno = CTkEntry(master=app, width=30, height=30, font=("Dubai", 15, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, uno, dos)), "%S"), insertontime=0, textvariable=solo_uno1)
uno.place(relx=0.05, rely=0.3)
def set_focus():
    uno.focus()
app.after(300, set_focus)

dos = CTkEntry(master=app, width=30, height=30, font=("Dubai", 15, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, dos, tres)), "%S"), insertontime=0, textvariable=solo_uno2)
dos.place(relx=0.2, rely=0.3)

tres = CTkEntry(master=app, width=30, height=30, font=("Dubai", 15, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, tres, cuatro)), "%S"), insertontime=0, textvariable=solo_uno3)
tres.place(relx=0.35, rely=0.3)

cuatro = CTkEntry(master=app, width=30, height=30, font=("Dubai", 15, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, cuatro, cinco)), "%S"), insertontime=0, textvariable=solo_uno4)
cuatro.place(relx=0.5, rely=0.3)

cinco = CTkEntry(master=app, width=30, height=30, font=("Dubai", 15, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, cinco, seis)), "%S"), insertontime=0, textvariable=solo_uno5)
cinco.place(relx=0.65, rely=0.3)

seis = CTkEntry(master=app, width=30, height=30, font=("Dubai", 15, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, seis, boton)), "%S"), insertontime=0, textvariable=solo_uno6)
seis.place(relx=0.8, rely=0.3)



boton = CTkButton(master=app, width=80, text="OK")
boton.place(relx=0.5, rely=0.75, anchor=CENTER)





uno.bind("<Key>", lambda event: borrar_y_mover(event, uno, uno))
dos.bind("<Key>", lambda event: borrar_y_mover(event, dos, uno))
tres.bind("<Key>", lambda event: borrar_y_mover(event, tres, dos))
cuatro.bind("<Key>", lambda event: borrar_y_mover(event, cuatro, tres))
cinco.bind("<Key>", lambda event: borrar_y_mover(event, cinco, cuatro))
seis.bind("<Key>", lambda event: borrar_y_mover(event, seis, cinco))
boton.bind("<Key>", lambda event: borrar_y_mover(event, boton, seis))


# for entry in (uno, dos, tres, cuatro, cinco, seis):
#     entry.bind("<FocusIn>", lambda event: entry.select_range(0, END))

root.mainloop()