from tkinter import *
import random
import pyperclip



def click():
    try:
        uno = int(input1.get())
        dos = int(input2.get())
        salidaTexto = ""

        caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!?,.-:;+()$&"

        __contraseña = ""
        cont = 1
        for i in range(uno):
            for i in range(dos):
                __contraseña += random.choice(caracteres)
                if len(__contraseña.replace("\n", "")) == (dos * cont):
                    cont += 1
                    __contraseña += "\n"

        if uno == 1:
            salidaTexto = ("\nAquí tienes tu contraseña personalizada:\n"+__contraseña+"\n")
        if uno > 1:
            salidaTexto = ("\nAquí tienes tus contraseñas personalizadas:\n"+__contraseña+"\n")

        msg3 = Label(ventana,  text = salidaTexto, bg="grey25", fg = "grey75", font = ("MS Reference Sans Serif", 7, "bold"))
        msg3.place(x = 36, y = 270)

        def copiar():
            pyperclip.copy(__contraseña)

        botonCopiar = Button(ventana, text = "Copiar contraseña/s", width=60, height=4, border="0", bg="blue4", fg="grey75", font = ("MS Reference Sans Serif", 9, "bold"), command = copiar)
        botonCopiar.pack(side = BOTTOM)
    except:
        salidaTexto = Label(ventana, text = "\nHas introducido un valor incorrecto. Vuelve a intentarlo", bg="grey25", fg = "white", font = ("MS Reference Sans Serif", 6, "bold"))
        salidaTexto.place(x = 15, y = 270)

#-------------------------------------------------------------------------------------------------------------------------------------------------

ventana = Tk()
ventana.title("Generador de contraseñas")
ventana.config(bg="gray25")
ventana.geometry("330x500")
ventana.resizable(0,1) 
ventana.iconbitmap(r"C:\Users\MARTI\Desktop\PYTHON\INTERFACES GRÁFICAS\contraseña.ico")

# frame = Frame()
# frame.pack()
# frame.config(bg = "blue")

etiqueta = Label(ventana, text = "\nGenerador de contraseñas seguras\n", bg="grey25", fg = "white", font = ("MS Reference Sans Serif", 12, "bold"))
etiqueta.pack()

msg1 = Label(ventana, text = "¿Cuántas contraseñas quieres crear?", bg="grey25", fg = "grey75", font = ("MS Reference Sans Serif", 7, "bold"))
msg1.place(x = 20, y = 75)
input1 = Entry(ventana, bg="grey20", fg = "grey75", justify = CENTER,font = ("MS Reference Sans Serif", 7, "bold"), width=4)
input1.place(x = 250, y = 78)

msg2 = Label(ventana, text = "\n¿De cuántos caracteres las quieres?", bg="grey25", fg = "grey75", font = ("MS Reference Sans Serif", 7, "bold"))
msg2.place(x = 20, y = 100)
input2 = Entry(ventana, bg="grey20", fg = "grey75", justify = CENTER ,font = ("MS Reference Sans Serif", 7, "bold"), width=4)
input2.place(x = 250, y = 112)  

requisitos = Label(ventana, text ="Seleccione los requisitos que necesitan sus contraseñas:", bg="grey25", fg = "grey75", justify = CENTER ,font = ("MS Reference Sans Serif", 6, "bold"))
requisitos.place(x = 20, y = 150)

botMin = Checkbutton(ventana, text = "minúscula", width=9, height=1, border="0", bg="grey20", fg="grey75", font = ("MS Reference Sans Serif", 5, "bold"))
botMin.place(x = 20, y = 170)
botMay = Checkbutton(ventana, text = "mayúscula", width=9, height=1, border="0", bg="gray20", fg="grey75", font = ("MS Reference Sans Serif", 5, "bold"))
botMay.place(x = 90, y = 170)
botNum = Checkbutton(ventana, text = "número", width=7, height=1, border="0", bg="gray20", fg="grey75", font = ("MS Reference Sans Serif", 5, "bold"))
botNum.place(x = 160, y = 170)
botCE = Checkbutton(ventana, text = "caracter especial", width=15, height=1, border="0", bg="gray20", fg="grey75", font = ("MS Reference Sans Serif", 5, "bold"))
botCE.place(x = 220, y = 170)

boton = Button(ventana, text = "Generar contraseñas", width=20, height=3, border="0", bg="forest green", fg="grey75", font = ("MS Reference Sans Serif", 7, "bold"), command = click)
boton.place(x = 100, y = 220)






ventana.mainloop()