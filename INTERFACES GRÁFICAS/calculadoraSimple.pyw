# CALCULADORA INACABADA !!

from tkinter import *

raiz = Tk()
raiz.config(bg = "red")
raiz.title("Calculadora")
raiz.resizable(0,0)

app = Frame(raiz, bg="navy")
app.pack(fill="both", expand=1)

# ------------------- funciones -----------------------------------------------------------------------------------

operacion = ""
resetPantalla = False
resultado = 0

numeroPantalla = StringVar()

def numeroPulsado(num):
    global operacion
    global resetPantalla

    if resetPantalla != False:
        numeroPantalla.set(num)
        resetPantalla = False
    else:
        numeroPantalla.set(numeroPantalla.get() + num)

def suma(num):
    global operacion
    global resultado
    global resetPantalla

    resultado += int(num)
    operacion = "suma"
    resetPantalla = True
    numeroPantalla.set(resultado)

num1 = 0
contadorResta = 0
def resta(num):
    global operacion
    global resultado
    global resetPantalla
    global num1
    global contadorResta

    if contadorResta == 0:
        num1 = int(num)
        resultado = num1
    else:
        if contadorResta == 1:
            resultado = num1 - int(num)
        else:
            resultado = int(resultado) - int(num)
        numeroPantalla.set(resultado)
        resultado = numeroPantalla.get()

    contadorResta += 1
    operacion = "resta"
    resetPantalla = True

contadorMulti = 0
def multiplicacion(num):
    global operacion
    global resultado
    global resetPantalla
    global num1
    global contadorMulti

    if contadorMulti == 0:
        num1 = int(num)
        resultado = num1
    else:
        if contadorMulti == 1:
            resultado = num1 * int(num)
        else:
            resultado = int(resultado) * int(num)
        numeroPantalla.set(resultado)
        resultado = numeroPantalla.get()

    contadorMulti += 1
    operacion = "multiplicacion"
    resetPantalla = True

contadorDiv = 0
def division(num):
    global operacion
    global resultado
    global resetPantalla
    global num1
    global contadorDiv

    if contadorDiv == 0:
        num1 = float(num)
        resultado = num1
    else:
        if contadorDiv == 1:
            resultado = num1 / float(num)
        else:
            resultado = float(resultado) / float(num)
        numeroPantalla.set(resultado)
        resultado = numeroPantalla.get()

    contadorDiv += 1
    operacion = "division"
    resetPantalla = True
    
def igual():
    global resultado
    global operacion
    global contadorResta
    global contadorMulti
    global contadorDiv
    
    if operacion == "suma":
        numeroPantalla.set(resultado+int(numeroPantalla.get()))
        resultado = 0

    elif operacion == "resta":
        numeroPantalla.set(resultado-int(numeroPantalla.get()))
        resultado = 0
        contadorResta = 0

    elif operacion == "multiplicacion":
        numeroPantalla.set(resultado*int(numeroPantalla.get()))
        resultado = 0
        contadorMulti = 0

    elif operacion == "division":
        numeroPantalla.set(resultado/int(numeroPantalla.get()))
        resultado = 0
        contadorDiv = 0

# ------------------- pantalla -----------------------------------------------------------------------------------

pantalla = Entry(app, bg="navy", fg="white",  width=8, bd=0, justify="right", font=("",30), insertbackground="white", textvariable=numeroPantalla)
pantalla.grid(row=0,column=0,columnspan=4)

# ------------------- fila 1 -----------------------------------------------------------------------------------

botonAC = Button(app, bg="medium blue", fg="white",  width=5, height=2, text="AC", padx=0)
botonAC.grid(row=1,column=0, sticky="nw")

botonParentesis1 = Button(app, bg="medium blue", fg="white",  width=5, height=2, text="(", padx=0)
botonParentesis1.grid(row=1,column=1, sticky="nw")

botonParentesis2 = Button(app, bg="medium blue", fg="white",  width=5, height=2, text=")", padx=0)
botonParentesis2.grid(row=1,column=2, sticky="nw")

botonBorrar = Button(app, bg="medium blue", fg="white",  width=5, height=2, text="Borrar", padx=0)
botonBorrar.grid(row=1,column=3, sticky="nw")

# ------------------- fila 2 -----------------------------------------------------------------------------------

boton7 = Button(app, bg="navy", fg="white",  width=5, height=2, text="7", padx=0, command=lambda:numeroPulsado("7"))
boton7.grid(row=2,column=0, sticky="nw")

boton8 = Button(app, bg="navy", fg="white",  width=5, height=2, text="8", padx=0, command=lambda:numeroPulsado("8"))
boton8.grid(row=2,column=1, sticky="nw")

boton9 = Button(app, bg="navy", fg="white",  width=5, height=2, text="9", padx=0, command=lambda:numeroPulsado("9"))
boton9.grid(row=2,column=2, sticky="nw")

botonD = Button(app, bg="dark green", fg="white",  width=5, height=2, text="÷", padx=0, command=lambda:division(numeroPantalla.get()))
botonD.grid(row=2,column=3, sticky="nw")

# ------------------- fila 3 -----------------------------------------------------------------------------------

boton4 = Button(app, bg="navy", fg="white",  width=5, height=2, text="4", padx=0, command=lambda:numeroPulsado("4"))
boton4.grid(row=3,column=0, sticky="nw")

boton5 = Button(app, bg="navy", fg="white",  width=5, height=2, text="5", padx=0, command=lambda:numeroPulsado("5"))
boton5.grid(row=3,column=1, sticky="nw")

boton6 = Button(app, bg="navy", fg="white",  width=5, height=2, text="6", padx=0, command=lambda:numeroPulsado("6"))
boton6.grid(row=3,column=2, sticky="nw")

botonM = Button(app, bg="dark green", fg="white",  width=5, height=2, text="×", padx=0, command=lambda:multiplicacion(numeroPantalla.get()))  
botonM.grid(row=3,column=3, sticky="nw")

# ------------------- fila 4 -----------------------------------------------------------------------------------

boton1 = Button(app, bg="navy", fg="white",  width=5, height=2, text="1", padx=0, command=lambda:numeroPulsado("1"))  
boton1.grid(row=4,column=0, sticky="nw")

boton2 = Button(app, bg="navy", fg="white",  width=5, height=2, text="2", padx=0, command=lambda:numeroPulsado("2"))  
boton2.grid(row=4,column=1, sticky="nw")

boton3 = Button(app, bg="navy", fg="white",  width=5, height=2, text="3", padx=0, command=lambda:numeroPulsado("3"))  
boton3.grid(row=4,column=2, sticky="nw")

botonR = Button(app, bg="dark green", fg="white",  width=5, height=2, text="-", padx=0, command=lambda:resta(numeroPantalla.get()))  
botonR.grid(row=4,column=3, sticky="nw")

# ------------------- fila 5 -----------------------------------------------------------------------------------

botonI = Button(app, bg="dark green", fg="white",  width=5, height=2, text="=", padx=0, command=lambda:igual())
botonI.grid(row=5,column=0, sticky="nw")

boton0 = Button(app, bg="navy", fg="white",  width=5, height=2, text="0", padx=0, command=lambda:numeroPulsado("0"))  
boton0.grid(row=5,column=1, sticky="nw")

botonC = Button(app, bg="navy", fg="white",  width=5, height=2, text=",", padx=0, command=lambda:numeroPulsado("."))  
botonC.grid(row=5,column=2, sticky="nw")

botonS = Button(app, bg="dark green", fg="white",  width=5, height=2, text="+", padx=0, command=lambda:suma(numeroPantalla.get()))  
botonS.grid(row=5,column=3, sticky="nw")


raiz.mainloop()