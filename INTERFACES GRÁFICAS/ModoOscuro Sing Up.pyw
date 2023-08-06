from tkinter import *

def modoOscuroClaro():
    if ape["bg"] == "white":
        ape.config(bg = "black")
        titulo.config(bg = "black", fg = "white")
        nombreLabel.config(bg = "black", fg = "white")
        apellidoLabel.config(bg = "black", fg = "white")
        emailLabel.config(bg = "black", fg = "white")
        nombreEntry.config(bg = "black", fg = "white", insertbackground="white")
        apellidoEntry.config(bg = "black", fg = "white", insertbackground="white")
        emailEntry.config(bg = "black", fg = "white", insertbackground="white")
        contraseñaLabel.config(bg = "black", fg = "white")
        contraseñaEntry.config(bg = "black", fg = "white", insertbackground="white")
        mostrarContraseña.config(bg = "black", fg="grey50")
        singUpButton.config(bg="gray10", fg="white")
        botonModoClaroOscuro.config(bg="black")
        botonModoClaroOscuro.config(image=fotoModoClaro)            

    elif ape["bg"] == "black":
        ape.config(bg = "white")
        titulo.config(bg = "white", fg = "black")
        nombreLabel.config(bg = "white", fg = "black")
        apellidoLabel.config(bg = "white", fg = "black")
        emailLabel.config(bg = "white", fg = "black")
        nombreEntry.config(bg = "white", fg = "black", insertbackground="black")
        apellidoEntry.config(bg = "white", fg = "black", insertbackground="black")
        emailEntry.config(bg = "white", fg = "black", insertbackground="black")
        contraseñaLabel.config(bg = "white", fg = "black")
        contraseñaEntry.config(bg = "white", fg = "black", insertbackground="black")
        mostrarContraseña.config(bg = "white", fg = "black")
        singUpButton.config(bg="gray90", fg="black")
        botonModoClaroOscuro.config(bg="white")
        botonModoClaroOscuro.config(image=fotoModoOscuro)


def showPass():
    if contraseñaEntry.cget("show") == "*":
        contraseñaEntry.config(show="")
    else:
        contraseñaEntry.config(show="*")


def singUp():
    nombreUsuario = nombreEntry.get()
    apellidoUsuario = apellidoEntry.get()
    emailUsuario = emailEntry.get()
    contraseñaUsuario = contraseñaEntry.get()


    colorFondo = ape["bg"]
    if colorFondo == "black":
        colorLetras = "white"
    elif colorFondo == "white":
        colorLetras = "black"

   

    if nombreUsuario != "" and apellidoUsuario != "" and emailUsuario != "" and contraseñaUsuario != "":
        arroba = 0
        punto = 0
        for i in range(len(emailUsuario)):
            if emailUsuario[i] == "@":
                arroba += 1
            if emailUsuario[i] == ".":
                punto += 1

        if arroba == 1:
            arrobaok = True
        else:
            arrobaok = False

        if punto >= 1:
            puntook = True
        else:
            puntook = False

        if arrobaok != True or puntook != True:
            if arrobaok == False and puntook == False:
                errorCorreoArrobaPunto = Label(ape, text = "Your email needs to have:\nan at (@)\nand at least one dot (.)", bg=colorFondo, fg="red", font=("MS Reference Sans Serif", 10), justify="left")
                errorCorreoArrobaPunto.grid(row=9, column=1, columnspan=5, sticky="w")
            if arrobaok == False and puntook == True:
                errorCorreoArroba = Label(ape, text = "Your email needs to have:\nan at (@)", bg=colorFondo, fg="red", font=("MS Reference Sans Serif", 10), justify="left")
                errorCorreoArroba.grid(row=9, column=1, columnspan=5, sticky="w")
            if puntook == False and arrobaok == True:
                errorCorreoPunto = Label(ape, text = "Your email needs to have:\nat least one dot (.)", bg=colorFondo, fg="red", font=("MS Reference Sans Serif", 10), justify="left")
                errorCorreoPunto.grid(row=9, column=1, columnspan=5, sticky="w")

        else:
            ape.destroy()
            ape2 = Frame(raiz, width=1000, height=600, bg="white")
            ape2.pack(fill = "both", expand=True)
            welcomeLabel = Label(ape2, text = "You singed up correctly. Thank you.", bg=colorFondo, fg=colorLetras, font=("MS Reference Sans Serif", 20))
            welcomeLabel.grid(row=0, column=0) 

    else:
        errorLabel = Label(ape, text = "There was an error\nin your registration,\nplease try again", bg=colorFondo, fg="red", font=("MS Reference Sans Serif", 10), justify="left")
        errorLabel.grid(row=9, column=1, columnspan=5, sticky="w")

# ------------------------------------------------------------------------------------------------------------------------------------------------

raiz = Tk()
raiz.title("Prueba Sing Up")
raiz.config(bg = "blue")

ape = Frame(raiz, width=1000, height=600, bg="white")
ape.pack(fill = "both", expand=True)


titulo = Label(ape, text="Sing up here", font=("MS Reference Sans Serif", 30),bg = "white")
titulo.grid(row=0,column=0, columnspan=2)

nombreLabel = Label(ape, text = "First name:", font=("MS Reference Sans Serif", 10),bg = "white")
nombreLabel.grid(row=3, column=0, sticky="w")

apellidoLabel = Label(ape, text = "Last name:", font=("MS Reference Sans Serif", 10),bg = "white")
apellidoLabel.grid(row=4, column=0, sticky="w")

emailLabel = Label(ape, text = "Email:", font=("MS Reference Sans Serif", 10),bg = "white")
emailLabel.grid(row=5, column=0, sticky="w")

contraseñaLabel = Label(ape, text="Password:", font=("MS Reference Sans Serif", 10),bg = "white")
contraseñaLabel.grid(row=6, column=0, sticky="w")



nombreEntry = Entry(ape, font=("MS Reference Sans Serif", 10),bg = "white")
nombreEntry.grid(row=3, column=1)

apellidoEntry = Entry(ape, font=("MS Reference Sans Serif", 10),bg = "white")
apellidoEntry.grid(row=4, column=1)

emailEntry = Entry(ape, font=("MS Reference Sans Serif", 10),bg = "white")
emailEntry.grid(row=5, column=1)

contraseñaEntry = Entry(ape, font=("MS Reference Sans Serif", 10),bg = "white", show="•")
contraseñaEntry.grid(row=6, column=1)

mostrarContraseña = Checkbutton(ape, text = "Show password", font=("MS Reference Sans Serif", 8), bg="white", cursor="hand2", command=showPass)
mostrarContraseña.grid(row=7, column=1, sticky="w")

singUpButton = Button(ape, width=11, height=1, text="Sing Up", bg = "gray90", font=("MS Reference Sans Serif", 10, "bold"), cursor="hand2", command=singUp)
singUpButton.grid(row=8, column=1, sticky="w")

fotoModoClaro=PhotoImage(file = r"C:\Users\MARTI\Desktop\PYTHON\INTERFACES GRÁFICAS\light-mode.png")
fotoModoOscuro=PhotoImage(file = r"C:\Users\MARTI\Desktop\PYTHON\INTERFACES GRÁFICAS\dark-mode.png") 
botonModoClaroOscuro = Button(ape,width=25,height=25, bg = "white",border=0, image=fotoModoOscuro, cursor="hand2", command=modoOscuroClaro)
botonModoClaroOscuro.grid(row=9, column=0, sticky="ws")











raiz.mainloop()