from tkinter import *
from sqlite3 import *





def singUp():
    global raiz
    raiz.destroy()

    raiz = Tk()
    raiz.title("Registrarse")
    raiz.config(bg="red")
    raiz.resizable(width=0, height=0)
  
    #  Obtenemos el largo y  ancho de la pantalla
    wtotal = raiz.winfo_screenwidth()
    htotal = raiz.winfo_screenheight()
    #  Guardamos el largo y alto de la ventana
    wventana = 620
    hventana = 450
    #  Aplicamos la siguiente formula para calcular donde debería posicionarse
    pwidth = round(wtotal/2-wventana/2)
    pheight = round(htotal/2-hventana/2)
    #  Se lo aplicamos a la geometría de la ventana
    raiz.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))


    app2 = Frame(raiz, bg="lightgrey")
    app2.pack(fill = "both", expand=True)

    swoosh = PhotoImage(file = r"C:\Users\MARTI\Desktop\PYTHON\INTERFACES GRÁFICAS\swoosh.png")
    fotoLogo = Label(app2,width=320,height=450, bg = "royalblue1",border=0, image=swoosh)
    fotoLogo.grid(row=0, column=1, rowspan=500, sticky="nw")

    tituloLabel = Label(app2, width=20,height=2, text="Registrarse", font=("Dubai", 20, "bold"), bg = "lightgrey", padx=0, pady=0)
    tituloLabel.grid(row=0, column=0, sticky="n")

    nombreLabel = Label(app2, text="Nombre:", font=("Dubai", 11), bg = "lightgrey", anchor="nw", padx=20)
    nombreLabel.grid(row=1, column=0, sticky="w")

    nombreEntry = Entry(app2, font=("Dubai", 11), width=33)
    nombreEntry.grid(row=2, column=0)

    apellidoLabel = Label(app2, text="Apellido:", font=("Dubai", 11), bg = "lightgrey", anchor="nw", padx=20)
    apellidoLabel.grid(row=3, column=0, sticky="w")

    apellidoEntry = Entry(app2, font=("Dubai", 11), width=33)
    apellidoEntry.grid(row=4, column=0)

    emailLabel = Label(app2, text="Email:", font=("Dubai", 11), bg = "lightgrey", anchor="nw", padx=20)
    emailLabel.grid(row=5, column=0, sticky="w")

    emailEntry = Entry(app2, font=("Dubai", 11), width=33)
    emailEntry.grid(row=6, column=0)

    contraseñaLabel = Label(app2, text="Contraseña:", font=("Dubai", 11), bg = "lightgrey", anchor="nw", padx=20)
    contraseñaLabel.grid(row=7, column=0, sticky="w")

    contraseñaEntry = Entry(app2, font=("Dubai", 11), width=33)
    contraseñaEntry.grid(row=8, column=0)

    Label(app2, text="", bg = "lightgrey").grid(row=9, column=0, sticky="n")

    enviarBoton = Button(app2, text="Registrarse", font=("Dubai", 11), bg = "royalblue1", fg="black", width=32, anchor="center", bd=0, cursor="hand2")
    enviarBoton.grid(row=10, column=0)


    logInLabel = Label(app2, text="Ya tienes una cuenta?", font=("Dubai", 8), bg="lightgrey", fg="black", padx=20)
    logInLabel.grid(row=11, column=0, sticky="w")
    logInButon = Button(app2, text="Inicia sesión aquí", font=("Dubai", 8), bg="lightgrey", fg="royalblue1", bd=0, cursor="hand2", command=logIn)
    logInButon.grid(row=11, column=0)

    #  BBDD
    # miCursor.execute("CREATE TABLE CLIENTES (ID INTEGER PRIMARY KEY AUTOINCREMENT, NOMBRE VARCHAR(50), APELLIDO VARCHAR(50), CORREO VARCHAR(75), CONTRASENA VARCHAR(50))")




    

def logIn():
    global raiz
    raiz.destroy()

    raiz = Tk()
    raiz.title("Inicio de sesión")
    raiz.config(bg="red")
    raiz.resizable(width=0, height=0)


    #  Obtenemos el largo y  ancho de la pantalla
    wtotal = raiz.winfo_screenwidth()
    htotal = raiz.winfo_screenheight()
    #  Guardamos el largo y alto de la ventana
    wventana = 620
    hventana = 450
    #  Aplicamos la siguiente formula para calcular donde debería posicionarse
    pwidth = round(wtotal/2-wventana/2)
    pheight = round(htotal/2-hventana/2)
    #  Se lo aplicamos a la geometría de la ventana
    raiz.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

    
    app = Frame(raiz, bg="lightgrey")
    app.pack(fill = "both", expand=True)


    swoosh = PhotoImage(file = r"C:\Users\MARTI\Desktop\PYTHON\INTERFACES GRÁFICAS\swoosh.png")
    fotoLogo = Label(app,width=310,height=450, bg = "royalblue1",border=0, image=swoosh)
    fotoLogo.grid(row=0, column=0, rowspan=500, sticky="n")

    tituloLabel = Label(app, width=20,height=3, text="Inicio de sesión", font=("Dubai", 20, "bold"), bg = "lightgrey", padx=0, pady=0)
    tituloLabel.grid(row=0, column=1, sticky="n")

    usuarioLabel = Label(app, text="Email:", font=("Dubai", 11), bg = "lightgrey", anchor="nw", padx=20)
    usuarioLabel.grid(row=1, column=1, sticky="w")

    usuarioEntry = Entry(app, font=("Dubai", 11), width=33)
    usuarioEntry.grid(row=2, column=1)

    Label(app, text="", bg = "lightgrey").grid(row=3, column=1, sticky="n")

    contraseñaLabel = Label(app, text="Contraseña:", font=("Dubai", 11), bg = "lightgrey", anchor="nw", padx=20)
    contraseñaLabel.grid(row=4, column=1, sticky="w")

    contraseñaEntry = Entry(app, font=("Dubai", 11), width=33)
    contraseñaEntry.grid(row=5, column=1)

    Label(app, text="", bg = "lightgrey").grid(row=6, column=1, sticky="n")
    Label(app, text="", bg = "lightgrey").grid(row=7, column=1, sticky="n")

    entrarBoton = Button(app, text="Iniciar sesión", font=("Dubai", 11), bg = "royalblue1", fg="black", width=32, anchor="center", bd=0, cursor="hand2")
    entrarBoton.grid(row=8, column=1)

    singUpLabel = Label(app, text="Aun no tienes una cuenta?", font=("Dubai", 8), bg="lightgrey", fg="black")
    singUpLabel.grid(row=9, column=1)
    singUpButon = Button(app, text="Registrate aquí", font=("Dubai", 8), bg="lightgrey", fg="royalblue1", bd=0, cursor="hand2", padx=20, command=singUp)
    singUpButon.grid(row=9, column=1, sticky="e")

# -----------------------------------------------------------------------------------------------------------------------------------------------

raiz = Tk()
raiz.title("Inicio de sesión")
raiz.config(bg="red")
raiz.resizable(width=0, height=0)

#  Obtenemos el largo y  ancho de la pantalla
wtotal = raiz.winfo_screenwidth()
htotal = raiz.winfo_screenheight()
#  Guardamos el largo y alto de la ventana
wventana = 620
hventana = 450
#  Aplicamos la siguiente formula para calcular donde debería posicionarse
pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)
#  Se lo aplicamos a la geometría de la ventana
raiz.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))


app = Frame(raiz, bg="lightgrey")
app.pack(fill = "both", expand=True)


def entrarLogIn():
    #  BBDD
    miConexion = connect(r"C:\Users\MARTI\Desktop\PYTHON\BBDD\Clientes")
    miCursor = miConexion.cursor()

    miCursor.execute("SELECT CORREO FROM CLIENTES")
    usuarios = miCursor.fetchall()
    for usuario in usuarios:
        if usuario[0] == usuarioEntry.get():
            miCursor.execute("SELECT CONTRASENA FROM CLIENTES WHERE CORREO = '"+usuarioEntry.get()+"'")
            contraseñas = miCursor.fetchall()
            for contraseña in contraseñas:
                if contraseña[0] == contraseñaEntry.get():
                    global app
                    app.destroy()
                    app = Frame(raiz, bg="purple")
                    app.pack(fill = "both", expand=True)
                    Label(app, text="Has iniciado sesión correctamente", font=("Dubai", 20, "bold"), bg="purple").pack()
                else:
                    break

    miConexion.commit()
    miConexion.close()


swoosh = PhotoImage(file = r"C:\Users\MARTI\Desktop\PYTHON\INTERFACES GRÁFICAS\swoosh.png")
fotoLogo = Label(app,width=310,height=450, bg = "royalblue1",border=0, image=swoosh)
fotoLogo.grid(row=0, column=0, rowspan=500, sticky="nw")

tituloLabel = Label(app, width=20,height=3, text="Inicio de sesión", font=("Dubai", 20, "bold"), bg = "lightgrey", padx=0, pady=0)
tituloLabel.grid(row=0, column=1, sticky="n")

usuarioLabel = Label(app, text="Email:", font=("Dubai", 11), bg = "lightgrey", anchor="nw", padx=20)
usuarioLabel.grid(row=1, column=1, sticky="w")

usuarioEntry = Entry(app, font=("Dubai", 11), width=33, selectbackground="royalblue1")
usuarioEntry.grid(row=2, column=1)

Label(app, text="", bg = "lightgrey").grid(row=3, column=1, sticky="n")

contraseñaLabel = Label(app, text="Contraseña:", font=("Dubai", 11), bg = "lightgrey", anchor="nw", padx=20)
contraseñaLabel.grid(row=4, column=1, sticky="w")

contraseñaEntry = Entry(app, font=("Dubai", 11), width=33, selectbackground="royalblue1")
contraseñaEntry.grid(row=5, column=1)

Label(app, text="", bg = "lightgrey").grid(row=6, column=1, sticky="n")
Label(app, text="", bg = "lightgrey").grid(row=7, column=1, sticky="n")

entrarBoton = Button(app, text="Iniciar sesión", font=("Dubai", 11), bg = "royalblue1", fg="black", width=32, height=1, anchor="center", bd=0, cursor="hand2", command=entrarLogIn)
entrarBoton.grid(row=8, column=1)

singUpLabel = Label(app, text="Aun no tienes una cuenta?", font=("Dubai", 8), bg="lightgrey", fg="black")
singUpLabel.grid(row=9, column=1)
singUpButon = Button(app, text="Registrate aquí", font=("Dubai", 8), bg="lightgrey", fg="royalblue1", bd=0, cursor="hand2", padx=20, command=singUp)
singUpButon.grid(row=9, column=1, sticky="e")


raiz.mainloop()