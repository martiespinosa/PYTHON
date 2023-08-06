from tkinter import *
from customtkinter import *
from sqlite3 import *
from PIL import ImageTk, Image
from CTkMessagebox import CTkMessagebox

raiz = CTk()
raiz.title("Registrarse")
raiz.config(bg="red")
raiz.resizable(width=0, height=0)

#  Obtenemos el largo y  ancho de la pantalla
wtotal = raiz.winfo_screenwidth()
htotal = raiz.winfo_screenheight()
#  Guardamos el largo y alto de la ventana
wventana = 300
hventana = 400
#  Aplicamos la siguiente formula para calcular donde debería posicionarse
pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)
#  Se lo aplicamos a la geometría de la ventana
raiz.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

app = CTkFrame(raiz)
app.pack(fill = "both", expand=True)


def enviarCorreo(email): # script para enviar correo de confirmacion
    from email.message import EmailMessage
    import ssl
    import smtplib
    import random

    miConexion = connect(r"C:\Users\MARTI\Desktop\PYTHON\BBDD\Clientes")
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT CORREO FROM CLIENTES")
    correos = miCursor.fetchall()
    correo_registrado = False
    for correo in correos:
        if correo[0] == email:
            mensaje = CTkMessagebox(title="Error", message="Este correo ya está registrado", font=("Dubai", 12, "bold"), icon="cancel", width=300, height=180)
            correo_registrado = True
            break
    if not correo_registrado:
        codigo = random.randint(100000,999999)
        if nombreEntry.get() != "" and apellidoEntry.get() != "" and email != "" and contraseñaEntry.get() != "":
            global app
            app.destroy()
            app = CTkFrame(raiz)
            app.pack(fill = "both", expand=True)
            mensaje1 = CTkLabel(master = app, text="Comprueba tu correo electrónico", font=("Dubai", 20, "bold"))
            mensaje1.place(relx=0.5, rely=0.1, anchor = CENTER)
            mensaje2 = CTkLabel(master = app, text="Te hemos enviado un código con el que confirmar tu registro", font=("Dubai", 10, "bold"))
            mensaje2.place(relx=0.5, rely=0.25, anchor = CENTER)
            solo_numeros =  lambda text: text.isdecimal()
            maximo_seis = StringVar()
            codigoEntry = CTkEntry(master = app, placeholder_text="CÓDIGO", font=("Dubai", 15, "bold"), justify=CENTER, width=90, height=25, border_width=2, corner_radius=5, validate="key", validatecommand=(app.register(solo_numeros), "%S"), textvariable=maximo_seis)
            codigoEntry.place(relx=0.5, rely=0.35,  anchor = CENTER)
            enviarCodigoBoton = CTkButton(master = app, text="OK", font=("Dubai", 15, "bold"), width=90, height=25, anchor="center", cursor="hand2", command=lambda: confirmarRegistro(codigoEntry.get(), str(codigo)))
            enviarCodigoBoton.place(relx=0.5, rely=0.5, anchor = CENTER)

            def limitador(maximo_seis):
                if len(maximo_seis.get()) > 6:
                    maximo_seis.set(maximo_seis.get()[:6])
            maximo_seis.trace("w", lambda *args: limitador(maximo_seis))
                

            email_emisor = "martiespinosa99@gmail.com"
            email_contrasena = "kmmtcwfmepbxnite"

            email_receptor = email

            asunto = "Confirmación de registro"
            cuerpo = "Hola "+str(nombreEntry.get())+",\nEste es el código para confirmar tu registro:\n\n"+str(codigo)

            em = EmailMessage()
            em["From"] = email_emisor
            em["To"] = email_receptor
            em["Subject"] = asunto
            em.set_content(cuerpo)

            contexto = ssl.create_default_context()

            with smtplib.SMTP_SSL('smtp.gmail.com', 465, context = contexto) as srvr: 
                srvr.login(email_emisor, email_contrasena)
                srvr.sendmail(email_emisor, email_receptor, em.as_string())
        return

    miConexion.commit()
    miConexion.close()



def entrarLogIn(email, contrasena):  
    global app
    miConexion = connect(r"C:\Users\MARTI\Desktop\PYTHON\BBDD\Clientes")
    miCursor = miConexion.cursor()
    miCursor.execute("SELECT CORREO FROM CLIENTES")
    correos = miCursor.fetchall()
    for correo in correos:
        if correo[0] == email:
            miCursor.execute("SELECT CONTRASENA FROM CLIENTES WHERE CORREO = '"+email+"'")
            contrasenas = miCursor.fetchall()
            for contrasenaa in contrasenas:
                if contrasenaa[0] == contrasena:
                    app.destroy()
                    app = CTkFrame(raiz)
                    app.pack(fill = "both", expand=True)
                    
                    set_appearance_mode("dark")
                    set_default_color_theme("dark-blue")

                    mensaje = CTkLabel(master = app, text="Has iniciado sesión\ncorrectamente", font=("Dubai", 22, "bold"))
                    mensaje.place(relx=0.5, rely=0.1, anchor = CENTER)
                else:
                    CTkMessagebox(title="Error", message="La contraseña es incorrecta", font=("Dubai", 12, "bold"), icon="cancel", width=300, height=180)
                    break

    miConexion.commit()
    miConexion.close()




def cambiarLogIn():
    global app
    app.destroy()
    
    set_appearance_mode("dark")
    set_default_color_theme("dark-blue")

    # raiz = CTk()
    # raiz.title("Inicio de sesión")
    # raiz.config(bg="red")
    # raiz.resizable(width=0, height=0)

    # #  Obtenemos el largo y  ancho de la pantalla
    # wtotal = raiz.winfo_screenwidth()
    # htotal = raiz.winfo_screenheight()
    # #  Guardamos el largo y alto de la ventana
    # wventana = 300
    # hventana = 400
    # #  Aplicamos la siguiente formula para calcular donde debería posicionarse
    # pwidth = round(wtotal/2-wventana/2)
    # pheight = round(htotal/2-hventana/2)
    # #  Se lo aplicamos a la geometría de la ventana
    # raiz.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))

    app = CTkFrame(raiz)
    app.pack(fill = "both", expand=True)

    tituloLabel = CTkLabel(master = app, width=30,height=3, text="Inicio de sesión", font=("Dubai", 33, "bold"), padx=0, pady=0)
    tituloLabel.place(relx=0.5, rely=0.1, anchor = CENTER)

    emailEntry = CTkEntry(master = app, placeholder_text="EMAIL", font=("Dubai", 11, "bold"), width=250, height=25, border_width=2, corner_radius=5)
    emailEntry.place(relx=0.5, rely=0.25, anchor = CENTER)

    contraseñaEntry = CTkEntry(master = app, placeholder_text="CONTRASEÑA", font=("Dubai", 11, "bold"), width=250, height=25, border_width=2, corner_radius=5)
    contraseñaEntry.place(relx=0.5, rely=0.35,  anchor = CENTER)

    entrarBoton = CTkButton(master = app, text="INICIAR SESIÓN", font=("Dubai", 11, "bold"), width=250, height=25, anchor="center", cursor="hand2", command=lambda: entrarLogIn(emailEntry.get(), contraseñaEntry.get()))
    entrarBoton.place(relx=0.5, rely=0.5, anchor = CENTER)

    singUpLabel = CTkLabel(master = app, text="¿AÚN NO TIENES UNA CUENTA?", font=("Dubai", 10))
    singUpLabel.place(relx=0.32, rely=0.57, anchor = CENTER)
    singUpButon = CTkButton(app, text="REGISTRATE AQUÍ", font=("Dubai", 10, "bold"), width=15, height=1.5, cursor="hand2", fg_color="transparent", hover=False, text_color="#1f538d", command=cambiarSingUp)
    singUpButon.place(relx=0.56, rely=0.5409)





def cambiarSingUp():
    global app
    app.destroy()

    app = CTkFrame(raiz)
    app.pack(fill = "both", expand=True)

    set_appearance_mode("dark")
    set_default_color_theme("dark-blue")

    tituloLabel = CTkLabel(master = app, width=30,height=3, text="Registrarse", font=("Dubai", 33, "bold"), padx=0, pady=0)
    tituloLabel.place(relx=0.5, rely=0.1, anchor = CENTER)

    nombreEntry = CTkEntry(master = app, placeholder_text="NOMBRE", font=("Dubai", 11, "bold"), width=250, height=25, border_width=2, corner_radius=5)
    nombreEntry.place(relx=0.5, rely=0.25, anchor = CENTER)

    apellidoEntry = CTkEntry(master = app, placeholder_text="APELLIDO", font=("Dubai", 11, "bold"), width=250, height=25, border_width=2, corner_radius=5)
    apellidoEntry.place(relx=0.5, rely=0.35, anchor = CENTER)

    emailEntry = CTkEntry(master = app, placeholder_text="EMAIL", font=("Dubai", 11, "bold"), width=250, height=25, border_width=2, corner_radius=5)
    emailEntry.place(relx=0.5, rely=0.45, anchor = CENTER)

    contraseñaEntry = CTkEntry(master = app, placeholder_text="CONTRASEÑA", font=("Dubai", 11, "bold"), width=250, height=25, border_width=2, corner_radius=5)
    contraseñaEntry.place(relx=0.5, rely=0.55, anchor = CENTER)


    enviarBoton = CTkButton(master=app, text="REGISTRARSE", font=("Dubai", 11, "bold"), width=250, height=25, anchor="center", cursor="hand2", command=lambda: enviarCorreo(emailEntry.get()))
    enviarBoton.place(relx=0.5, rely=0.7, anchor = CENTER)

    logInLabel = CTkLabel(master = app, text="¿YA TIENES UNA CUENTA?", font=("Dubai", 10))
    logInLabel.place(relx=0.28, rely=0.77, anchor = CENTER)
    logInButon = CTkButton(app, text="INICIA SESIÓN AQUÍ", font=("Dubai", 10, "bold"), width=15, height=1.5, cursor="hand2", fg_color="transparent", hover=False, text_color="#1f538d", command=cambiarLogIn)
    logInButon.place(relx=0.48, rely=0.7409)


def confirmarRegistro(codigoEntry, codigo):
    if codigoEntry == codigo:   

        #  BBDD
        miConexion = connect(r"C:\Users\MARTI\Desktop\PYTHON\BBDD\Clientes")
        miCursor = miConexion.cursor()
        miCursor.execute("CREATE TABLE IF NOT EXISTS CLIENTES (NOMBRE VARCHAR(50), APELLIDO VARCHAR(50), CORREO VARCHAR(75), CONTRASENA VARCHAR(50))")

        miConexion = connect(r"C:\Users\MARTI\Desktop\PYTHON\BBDD\Clientes")
        miCursor = miConexion.cursor()
        miCursor.execute("INSERT INTO CLIENTES VALUES(?, ?, ?, ?)", (nombreEntry.get(), apellidoEntry.get(), emailEntry.get(), contraseñaEntry.get()))
            
        miConexion.commit()
        miConexion.close()

        global app
        app.destroy()
        app = CTkFrame(raiz)
        app.pack(fill = "both", expand=True)
        
        set_appearance_mode("dark")
        set_default_color_theme("dark-blue")

        mensaje = CTkLabel(master = app, text="Te has registrado\ncorrectamente", font=("Dubai", 22, "bold"))
        mensaje.place(relx=0.5, rely=0.1, anchor = CENTER)
        return
    
    else:
        CTkMessagebox(title="Error", message="El código es incorrecto", font=("Dubai", 12, "bold"), icon="cancel", width=300, height=180)
        return

def showPass():
    pass



set_appearance_mode("dark")
set_default_color_theme("dark-blue")

tituloLabel = CTkLabel(master = app, width=30,height=3, text="Registrarse", font=("Dubai", 33, "bold"), padx=0, pady=0)
tituloLabel.place(relx=0.5, rely=0.1, anchor = CENTER)

global nombreEntry
nombreEntry = CTkEntry(master = raiz, placeholder_text="NOMBRE", font=("Dubai", 11, "bold"), width=250, height=25, border_width=2, corner_radius=5)
nombreEntry.place(relx=0.5, rely=0.25, anchor = CENTER)

global apellidoEntry
apellidoEntry = CTkEntry(master = raiz, placeholder_text="APELLIDO", font=("Dubai", 11, "bold"), width=250, height=25, border_width=2, corner_radius=5)
apellidoEntry.place(relx=0.5, rely=0.35, anchor = CENTER)

global emailEntry
emailEntry = CTkEntry(master = raiz, placeholder_text="EMAIL", font=("Dubai", 11, "bold"), width=250, height=25, border_width=2, corner_radius=5)
emailEntry.place(relx=0.5, rely=0.45, anchor = CENTER)

global contraseñaEntry
contraseñaEntry = CTkEntry(master = raiz, placeholder_text="CONTRASEÑA", font=("Dubai", 11, "bold"), show="•",  width=250, height=25, border_width=2, corner_radius=5)
contraseñaEntry.place(relx=0.5, rely=0.55, anchor = CENTER)

# mostrarContrasena = Checkbutton(master = raiz, text = "Mostrar contraseña", font=("Dubai", 8), cursor="hand2", command=showPass)
# mostrarContrasena.place(relx=0.1, rely=0.6, anchor = CENTER)


enviarBoton = CTkButton(master = app, text="REGISTRARSE", font=("Dubai", 11, "bold"), width=250, height=25, anchor="center", cursor="hand2", command=lambda: enviarCorreo(emailEntry.get()))
enviarBoton.place(relx=0.5, rely=0.7, anchor = CENTER)

logInLabel = CTkLabel(master = app, text="¿YA TIENES UNA CUENTA?", font=("Dubai", 10))
logInLabel.place(relx=0.28, rely=0.77, anchor = CENTER)
logInButon = CTkButton(app, text="INICIA SESIÓN AQUÍ", font=("Dubai", 10, "bold"), width=15, height=1.5, cursor="hand2", fg_color="transparent", hover=False, text_color="#1f538d", command=cambiarLogIn)
logInButon.place(relx=0.48, rely=0.7409)





raiz.mainloop()