from tkinter import *
from customtkinter import *
from sqlite3 import *

raiz = Tk()
raiz.title("Registrarse")
raiz.config(bg="red")
raiz.resizable(width=1, height=0)

#  Obtenemos el largo y  ancho de la pantalla
wtotal = raiz.winfo_screenwidth()
htotal = raiz.winfo_screenheight()
#  Guardamos el largo y alto de la ventana
wventana = 610
hventana = 450
#  Aplicamos la siguiente formula para calcular donde debería posicionarse
pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)
#  Se lo aplicamos a la geometría de la ventana
raiz.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

app = Frame(raiz, bg="lightgrey")
app.pack(fill = "both", expand=True)


def enviarCorreo(): # script para enviar correo de confirmacion
    from email.message import EmailMessage
    import ssl
    import smtplib

    email_emisor = "martiespinosa99@gmail.com"
    email_contrasena = "kmmtcwfmepbxnite"

    email_receptor = emailEntry.get()

    asunto = "Email de prueba"
    cuerpo = """
    Texto de ejemplo
    """

    em = EmailMessage()
    em["From"] = email_emisor
    em["To"] = email_receptor
    em["Subject"] = asunto
    em.set_content(cuerpo)

    contexto = ssl.create_default_context()

    with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = contexto) as server: 
        server.login(email_emisor, email_contrasena)
        server.sendmail(email_emisor, email_receptor, em.as_string())


def enviarSingUp():
    #  BBDD
    miConexion = connect(r"C:\Users\MARTI\Desktop\PYTHON\BBDD\Clientes")
    miCursor = miConexion.cursor()
    miCursor.execute("CREATE TABLE IF NOT EXISTS CLIENTES (NOMBRE VARCHAR(50), APELLIDO VARCHAR(50), CORREO VARCHAR(75), CONTRASENA VARCHAR(50))")

    nombre = nombreEntry.get()
    apellido = apellidoEntry.get()
    email = emailEntry.get()
    contraseña = contraseñaEntry.get()

    if nombre != "" and apellido != "" and email != "" and contraseña != "":
        miConexion = connect(r"C:\Users\MARTI\Desktop\PYTHON\BBDD\Clientes")
        miCursor = miConexion.cursor()
        miCursor.execute("INSERT INTO CLIENTES VALUES($nombre, $apellido, $correo, $contrasena)", (nombre, apellido, email, contraseña))
        
    miConexion.commit()
    miConexion.close()


swoosh = PhotoImage(file = r"C:\Users\MARTI\Desktop\PYTHON\INTERFACES GRÁFICAS\swoosh.png")
fotoLogo = Label(app,width=310,height=450, bg = "royalblue1",border=0, image=swoosh)
fotoLogo.grid(row=0, column=1, rowspan=500, sticky="nw")

tituloLabel = Label(app, width=20,height=2, text="Registrarse", font=("Dubai", 20, "bold"), bg = "lightgrey", padx=0, pady=0)
tituloLabel.grid(row=0, column=0, sticky="n")

nombreLabel = Label(app, text="Nombre:", font=("Dubai", 11), bg = "lightgrey", anchor="nw", padx=20)
nombreLabel.grid(row=1, column=0, sticky="w")

nombreEntry = Entry(app, font=("Dubai", 11), width=33)
nombreEntry.grid(row=2, column=0)

apellidoLabel = Label(app, text="Apellido:", font=("Dubai", 11), bg = "lightgrey", anchor="nw", padx=20)
apellidoLabel.grid(row=3, column=0, sticky="w")

apellidoEntry = Entry(app, font=("Dubai", 11), width=33)
apellidoEntry.grid(row=4, column=0)

emailLabel = Label(app, text="Email:", font=("Dubai", 11), bg = "lightgrey", anchor="nw", padx=20)
emailLabel.grid(row=5, column=0, sticky="w")

emailEntry = Entry(app, font=("Dubai", 11), width=33)
emailEntry.grid(row=6, column=0)

contraseñaLabel = Label(app, text="Contraseña:", font=("Dubai", 11), bg = "lightgrey", anchor="nw", padx=20)
contraseñaLabel.grid(row=7, column=0, sticky="w")

contraseñaEntry = Entry(app, font=("Dubai", 11), width=33)
contraseñaEntry.grid(row=8, column=0)

Label(app, text="", bg = "lightgrey").grid(row=9, column=0, sticky="n")

enviarBoton = Button(app, text="Registrarse", font=("Dubai", 11), bg = "royalblue1", fg="black", width=32, anchor="center", bd=0, cursor="hand2", command=enviarCorreo)
enviarBoton.grid(row=10, column=0)

logInLabel = Label(app, text="Ya tienes una cuenta?", font=("Dubai", 8), bg="lightgrey", fg="black", padx=20)
logInLabel.grid(row=11, column=0, sticky="w")
logInButon = Button(app, text="Inicia sesión aquí", font=("Dubai", 8), bg="lightgrey", fg="royalblue1", bd=0, cursor="hand2")
logInButon.grid(row=11, column=0)





raiz.mainloop()