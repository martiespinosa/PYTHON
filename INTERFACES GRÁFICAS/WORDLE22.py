from tkinter import *
from tkinter.ttk import *
from customtkinter import *
from sqlite3 import *
import random

root = Tk()
root.title("WORDLE")
root.geometry("350x500")
root.resizable(0, 0)

app = CTkFrame(master = root)
app.pack(fill=BOTH, expand=1)


#  Obtenemos el largo y  ancho de la pantalla
wtotal = root.winfo_screenwidth()
htotal = root.winfo_screenheight()
#  Guardamos el largo y alto de la ventana
wventana = 350
hventana = 500
#  Aplicamos la siguiente formula para calcular donde debería posicionarse
pwidth = round(wtotal/2-wventana/2)
pheight = round(htotal/2-hventana/2)
#  Se lo aplicamos a la geometría de la ventana
root.geometry(str(wventana)+"x"+str(hventana)+"+"+str(pwidth)+"+"+str(pheight))


solo_letras = lambda text: text.isalpha()
var_f1_c1 = StringVar()
var_f1_c2 = StringVar()
var_f1_c3 = StringVar()
var_f1_c4 = StringVar()
var_f1_c5 = StringVar()

var_f2_c1 = StringVar()
var_f2_c2 = StringVar()
var_f2_c3 = StringVar()
var_f2_c4 = StringVar()
var_f2_c5 = StringVar()

var_f3_c1 = StringVar()
var_f3_c2 = StringVar()
var_f3_c3 = StringVar()
var_f3_c4 = StringVar()
var_f3_c5 = StringVar()

var_f4_c1 = StringVar()
var_f4_c2 = StringVar()
var_f4_c3 = StringVar()
var_f4_c4 = StringVar()
var_f4_c5 = StringVar()

var_f5_c1 = StringVar()
var_f5_c2 = StringVar()
var_f5_c3 = StringVar()
var_f5_c4 = StringVar()
var_f5_c5 = StringVar()

var_f6_c1 = StringVar()
var_f6_c2 = StringVar()
var_f6_c3 = StringVar()
var_f6_c4 = StringVar()
var_f6_c5 = StringVar()



def validar_y_mover(event, entry_actual, entry_siguiente):
    if entry_actual != labelWordle and entry_siguiente != labelWordle and entry_actual.get() == "":
        entry_actual.focus_set()
    elif entry_actual != labelWordle and entry_siguiente != labelWordle and entry_actual.get() != "" and entry_siguiente.get() == "":
        entry_siguiente.focus_set()
        entry_siguiente = entry_actual
    elif entry_actual == labelWordle:
        labelWordle.focus_set()
        return False
    
    if solo_letras(event):
        entry_siguiente.focus_set()
        return solo_letras(event)
    return False



def borrar_y_mover(event, entry_actual, entry_anterior):
    if entry_actual != labelWordle and event.keysym == "BackSpace" and len(entry_actual.get()) == 0:
        entry_anterior.focus_set()
        entry_anterior.delete(0, END)
    elif entry_actual != labelWordle and event.keysym == "BackSpace" and len(entry_actual.get()) != 0:
        entry_actual.focus_set()
        entry_actual.delete(0, END)
    elif entry_actual == labelWordle and event.keysym == "BackSpace":
        if entry_f1_c5.get() != "" and entry_f2_c5.get() == "" and entry_f3_c5.get() == "" and entry_f4_c5.get() == "" and entry_f5_c5.get() == "" and entry_f6_c5.get() == "":
            entry_anterior = entry_f1_c5
        elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() == "" and entry_f4_c5.get() == "" and entry_f5_c5.get() == "" and entry_f6_c5.get() == "":
            entry_anterior = entry_f2_c5
        elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() != "" and entry_f4_c5.get() == "" and entry_f5_c5.get() == "" and entry_f6_c5.get() == "":
            entry_anterior = entry_f3_c5
        elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() != "" and entry_f4_c5.get() != "" and entry_f5_c5.get() == "" and entry_f6_c5.get() == "":
            entry_anterior = entry_f4_c5
        elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() != "" and entry_f4_c5.get() != "" and entry_f5_c5.get() != "" and entry_f6_c5.get() == "":
            entry_anterior = entry_f5_c5
        elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() != "" and entry_f4_c5.get() != "" and entry_f5_c5.get() != "" and entry_f6_c5.get() != "":
            entry_anterior = entry_f6_c5

        entry_anterior.delete(0, END)
        entry_anterior.focus_set()


def enter(event, entry_actual, entry_siguiente, entry_f1_c1, entry_f1_c2, entry_f1_c3, entry_f1_c4, entry_f1_c5, entry_f2_c1, entry_f2_c2, entry_f2_c3, entry_f2_c4, entry_f2_c5, entry_f3_c1, entry_f3_c2, entry_f3_c3, entry_f3_c4, entry_f3_c5, entry_f4_c1, entry_f4_c2, entry_f4_c3, entry_f4_c4, entry_f4_c5, entry_f5_c1, entry_f5_c2, entry_f5_c3, entry_f5_c4, entry_f5_c5, entry_f6_c1, entry_f6_c2, entry_f6_c3, entry_f6_c4, entry_f6_c5, palabraElejida):
    if entry_actual == labelWordle and event.keysym == "Return":
        global AA
        AA = 0
        global BB
        BB = 0
        global CC
        CC = 0
        global DD
        DD = 0
        global EE
        EE = 0
        global FF
        FF = 0
        global GG
        GG = 0
        global HH
        HH = 0
        global II
        II = 0
        global JJ
        JJ = 0
        global KK
        KK = 0
        global LL
        LL = 0
        global MM
        MM = 0
        global NN
        NN = 0
        global ÑÑ
        ÑÑ = 0
        global OO
        OO = 0
        global PP
        PP = 0
        global QQ
        QQ = 0
        global RR
        RR = 0
        global SS
        SS = 0
        global TT
        TT = 0
        global UU
        UU = 0
        global VV
        VV = 0
        global WW
        WW = 0
        global XX
        XX = 0
        global YY
        YY = 0
        global ZZ
        ZZ = 0

        for y in range(5):
            if palabraElejida[y] == "A":
                AA += 1
            if palabraElejida[y] == "B":
                BB += 1
            if palabraElejida[y] == "C":
                CC += 1
            if palabraElejida[y] == "D":
                DD += 1
            if palabraElejida[y] == "E":
                EE += 1
            if palabraElejida[y] == "F":
                FF += 1
            if palabraElejida[y] == "G":
                GG += 1
            if palabraElejida[y] == "H":
                HH += 1
            if palabraElejida[y] == "I":
                II += 1
            if palabraElejida[y] == "J":
                JJ += 1
            if palabraElejida[y] == "K":
                KK += 1
            if palabraElejida[y] == "L":
                LL += 1
            if palabraElejida[y] == "M":
                MM += 1
            if palabraElejida[y] == "N":
                NN += 1
            if palabraElejida[y] == "Ñ":
                ÑÑ += 1
            if palabraElejida[y] == "O":
                OO += 1
            if palabraElejida[y] == "P":
                PP += 1
            if palabraElejida[y] == "Q":
                QQ += 1
            if palabraElejida[y] == "R":
                RR += 1
            if palabraElejida[y] == "S":
                SS += 1
            if palabraElejida[y] == "T":
                TT += 1
            if palabraElejida[y] == "U":
                UU += 1
            if palabraElejida[y] == "V":
                VV += 1
            if palabraElejida[y] == "W":
                WW += 1
            if palabraElejida[y] == "X":
                XX += 1
            if palabraElejida[y] == "Y":
                YY += 1
            if palabraElejida[y] == "Z":
                ZZ += 1


        miConexion = connect(r"C:\Users\MARTI\Desktop\PYTHON\BBDD\palabrasWordle")
        miCursor = miConexion.cursor()
        miCursor.execute("SELECT PALABRA FROM PALABRAS")
        
        todasLasPalabras = miCursor.fetchall()
        
        miCursor.execute("SELECT MAX(id) FROM PALABRAS")
        global numeroPalabrasTotal
        numeroPalabrasTotal = miCursor.fetchone()[0]
                                    
        miConexion.commit()
        miConexion.close()

    
    
        if entry_f1_c5.get() != "" and entry_f2_c5.get() == "" and entry_f3_c5.get() == "" and entry_f4_c5.get() == "" and entry_f5_c5.get() == "" and entry_f6_c5.get() == "":
            global paraulaUsuari
            paraulaUsuari = entry_f1_c1.get() + entry_f1_c2.get() + entry_f1_c3.get() + entry_f1_c4.get() + entry_f1_c5.get()
            listaEntrys = [entry_f1_c1, entry_f1_c2, entry_f1_c3, entry_f1_c4, entry_f1_c5]
        elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() == "" and entry_f4_c5.get() == "" and entry_f5_c5.get() == "" and entry_f6_c5.get() == "":
            paraulaUsuari = entry_f2_c1.get() + entry_f2_c2.get() + entry_f2_c3.get() + entry_f2_c4.get() + entry_f2_c5.get()
            listaEntrys = [entry_f2_c1, entry_f2_c2, entry_f2_c3, entry_f2_c4, entry_f2_c5]
        elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() != "" and entry_f4_c5.get() == "" and entry_f5_c5.get() == "" and entry_f6_c5.get() == "":
            paraulaUsuari = entry_f3_c1.get() + entry_f3_c2.get() + entry_f3_c3.get() + entry_f3_c4.get() + entry_f3_c5.get()
            listaEntrys = [entry_f3_c1, entry_f3_c2, entry_f3_c3, entry_f3_c4, entry_f3_c5]
        elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() != "" and entry_f4_c5.get() != "" and entry_f5_c5.get() == "" and entry_f6_c5.get() == "":
            paraulaUsuari = entry_f4_c1.get() + entry_f4_c2.get() + entry_f4_c3.get() + entry_f4_c4.get() + entry_f4_c5.get()
            listaEntrys = [entry_f4_c1, entry_f4_c2, entry_f4_c3, entry_f4_c4, entry_f4_c5]
        elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() != "" and entry_f4_c5.get() != "" and entry_f5_c5.get() != "" and entry_f6_c5.get() == "":
            paraulaUsuari = entry_f5_c1.get() + entry_f5_c2.get() + entry_f5_c3.get() + entry_f5_c4.get() + entry_f5_c5.get()
            listaEntrys = [entry_f5_c1, entry_f5_c2, entry_f5_c3, entry_f5_c4, entry_f5_c5]
        elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() != "" and entry_f4_c5.get() != "" and entry_f5_c5.get() != "" and entry_f6_c5.get() != "":
            paraulaUsuari = entry_f6_c1.get() + entry_f6_c2.get() + entry_f6_c3.get() + entry_f6_c4.get() + entry_f6_c5.get()
            listaEntrys = [entry_f6_c1, entry_f6_c2, entry_f6_c3, entry_f6_c4, entry_f6_c5]


        
        for i in range(int(numeroPalabrasTotal)):
            todasLasPalabrasDeUnaEnUna = todasLasPalabras[i][0]
            if paraulaUsuari == todasLasPalabrasDeUnaEnUna:
                
                # VERDES
                for w in range(5):
                    if paraulaUsuari[w] == palabraElejida[w]:
                        listaEntrys[w].configure(fg_color="limegreen")
                        if listaEntrys[w].get() == "A":
                            AA -= 1
                        if listaEntrys[w].get() == "B":
                            BB -= 1
                        if listaEntrys[w].get() == "C":
                            CC -= 1
                        if listaEntrys[w].get() == "D":
                            DD -= 1
                        if listaEntrys[w].get() == "E":
                            EE -= 1
                        if listaEntrys[w].get() == "F":
                            FF -= 1
                        if listaEntrys[w].get() == "G":
                            GG -= 1
                        if listaEntrys[w].get() == "H":
                            HH -= 1
                        if listaEntrys[w].get() == "I":
                            II -= 1
                        if listaEntrys[w].get() == "J":
                            JJ -= 1
                        if listaEntrys[w].get() == "K":
                            KK -= 1
                        if listaEntrys[w].get() == "L":
                            LL -= 1
                        if listaEntrys[w].get() == "M":
                            MM -= 1
                        if listaEntrys[w].get() == "N":
                            NN -= 1
                        if listaEntrys[w].get() == "Ñ":
                            ÑÑ -= 1
                        if listaEntrys[w].get() == "O":
                            OO -= 1
                        if listaEntrys[w].get() == "P":
                            PP -= 1
                        if listaEntrys[w].get() == "Q":
                            QQ -= 1
                        if listaEntrys[w].get() == "R":
                            RR -= 1
                        if listaEntrys[w].get() == "S":
                            SS -= 1
                        if listaEntrys[w].get() == "T":
                            TT -= 1
                        if listaEntrys[w].get() == "U":
                            UU -= 1
                        if listaEntrys[w].get() == "V":
                            VV -= 1
                        if listaEntrys[w].get() == "W":
                            WW -= 1
                        if listaEntrys[w].get() == "X":
                            XX -= 1
                        if listaEntrys[w].get() == "Y":
                            YY -= 1
                        if listaEntrys[w].get() == "Z":
                            ZZ -= 1
                        
                # AMARILLAS
                for w in range(5):
                    if paraulaUsuari[w] != palabraElejida[w] and (paraulaUsuari[w] == palabraElejida[0] or paraulaUsuari[w] == palabraElejida[1] or paraulaUsuari[w] == palabraElejida[2] or paraulaUsuari[w] == palabraElejida[3] or paraulaUsuari[w] == palabraElejida[4]):
                        if paraulaUsuari[w] == "A":
                            if AA > 0:
                                listaEntrys[w].configure(fg_color="gold")
                                AA -= 1
                        if paraulaUsuari[w] == "B":
                            if BB > 0:
                                listaEntrys[w].configure(fg_color="gold")
                                BB -= 1
                        if paraulaUsuari[w] == "C":
                            if CC > 0:
                                listaEntrys[w].configure(fg_color="gold")
                                CC -= 1
                        if paraulaUsuari[w] == "D":
                            if DD > 0:
                                listaEntrys[w].configure(fg_color="gold")
                                DD -= 1
                        if paraulaUsuari[w] == "E":
                            if EE > 0:
                                listaEntrys[w].configure(fg_color="gold")
                                EE -= 1
                        if paraulaUsuari[w] == "F":
                            if FF > 0:
                                listaEntrys[w].configure(fg_color="gold")
                                FF -= 1
                        if paraulaUsuari[w] == "G":
                            if GG > 0:
                                listaEntrys[w].configure(fg_color="gold")
                                GG -= 1
                        if paraulaUsuari[w] == "H":
                            if HH > 0:
                                listaEntrys[w].configure(fg_color="gold")
                                HH -= 1
                        if paraulaUsuari[w] == "I":
                            if II > 0:
                                listaEntrys[w].configure(fg_color="gold")
                                II -= 1
                        if paraulaUsuari[w] == "J":
                            if JJ > 0:
                                listaEntrys[w].configure(fg_color="gold")
                                JJ -= 1
                        if paraulaUsuari[w] == "K":
                            if KK > 0:
                                listaEntrys[w].configure(fg_color="gold")
                                KK -= 1
                        if paraulaUsuari[w] == "L":
                            if LL > 0:
                                listaEntrys[w].configure(fg_color="gold")
                                LL -= 1
                        if paraulaUsuari[w] == "M":
                            if MM > 0:
                                listaEntrys[w].configure(fg_color="gold")
                                MM -= 1
                        if paraulaUsuari[w] == "N":
                            if NN > 0:
                                listaEntrys[w].configure(fg_color="gold")
                                NN -= 1
                        if paraulaUsuari[w] == "Ñ":
                            if ÑÑ > 0:
                                listaEntrys[w].configure(fg_color="gold")
                                ÑÑ -= 1
                        if paraulaUsuari[w] == "O":
                            if OO > 0:
                                listaEntrys[w].configure(fg_color="gold")
                                OO -= 1
                        if paraulaUsuari[w] == "P":
                            if PP > 0:
                                listaEntrys[w].configure(fg_color="gold")
                                PP -= 1
                        if paraulaUsuari[w] == "Q":
                            if QQ > 0:
                                listaEntrys[w].configure(fg_color="gold")
                                QQ -= 1
                        if paraulaUsuari[w] == "R":
                            if RR > 0:
                                listaEntrys[w].configure(fg_color="gold")
                                RR -= 1
                        if paraulaUsuari[w] == "S":
                            if SS > 0:
                                listaEntrys[w].configure(fg_color="gold")
                                SS -= 1
                        if paraulaUsuari[w] == "T":
                            if TT > 0:
                                listaEntrys[w].configure(fg_color="gold")
                                TT -= 1
                        if paraulaUsuari[w] == "U":
                            if UU > 0:
                                listaEntrys[w].configure(fg_color="gold")
                                UU -= 1
                        if paraulaUsuari[w] == "V":
                            if VV > 0:
                                listaEntrys[w].configure(fg_color="gold")
                                VV -= 1
                        if paraulaUsuari[w] == "W":
                            if WW > 0:
                                listaEntrys[w].configure(fg_color="gold")
                                WW -= 1
                        if paraulaUsuari[w] == "X":
                            if XX > 0:
                                listaEntrys[w].configure(fg_color="gold")
                                XX -= 1
                        if paraulaUsuari[w] == "Y":
                            if YY > 0:
                                listaEntrys[w].configure(fg_color="gold")
                                YY -= 1
                        if paraulaUsuari[w] == "Z":
                            if ZZ > 0:
                                listaEntrys[w].configure(fg_color="gold")
                                ZZ -= 1
                    
                    
 


                # pasar a la siguiente linea
                if entry_f1_c5.get() != "" and entry_f2_c5.get() == "" and entry_f3_c5.get() == "" and entry_f4_c5.get() == "" and entry_f5_c5.get() == "" and entry_f6_c5.get() == "":
                    entry_siguiente = entry_f2_c1
                elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() == "" and entry_f4_c5.get() == "" and entry_f5_c5.get() == "" and entry_f6_c5.get() == "":
                    entry_siguiente = entry_f3_c1
                elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() != "" and entry_f4_c5.get() == "" and entry_f5_c5.get() == "" and entry_f6_c5.get() == "":
                    entry_siguiente = entry_f4_c1
                elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() != "" and entry_f4_c5.get() != "" and entry_f5_c5.get() == "" and entry_f6_c5.get() == "":
                    entry_siguiente = entry_f5_c1
                elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() != "" and entry_f4_c5.get() != "" and entry_f5_c5.get() != "" and entry_f6_c5.get() == "":
                    entry_siguiente = entry_f6_c1
                elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() != "" and entry_f4_c5.get() != "" and entry_f5_c5.get() != "" and entry_f6_c5.get() != "":
                    return False
    
        
                entry_siguiente.focus_set()

# -------------------------------------------------------------------------------------------

labelWordle = CTkLabel(master=app, text="WORDLE", font=("Dubai", 33, "bold"), justify=CENTER)
labelWordle.place(relx=0.5, rely=0.1, anchor = CENTER)

# ------------ fila 1 ------------

entry_f1_c1 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f1_c1, entry_f1_c2)), "%S"), insertontime=0, textvariable=var_f1_c1)
entry_f1_c1.place(relx=0.15, rely=0.2)
entry_f1_c1.focus_set()

entry_f1_c2 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f1_c2, entry_f1_c3)), "%S"), insertontime=0, textvariable=var_f1_c2)
entry_f1_c2.place(relx=0.3, rely=0.2)

entry_f1_c3 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f1_c3, entry_f1_c4)), "%S"), insertontime=0, textvariable=var_f1_c3)
entry_f1_c3.place(relx=0.45, rely=0.2)

entry_f1_c4 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f1_c4, entry_f1_c5)), "%S"), insertontime=0, textvariable=var_f1_c4)
entry_f1_c4.place(relx=0.6, rely=0.2)

entry_f1_c5 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f1_c5, labelWordle)), "%S"), insertontime=0, textvariable=var_f1_c5)
entry_f1_c5.place(relx=0.75, rely=0.2)

# ------------ fila 2 ------------

entry_f2_c1 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f2_c1, entry_f2_c2)), "%S"), insertontime=0, textvariable=var_f2_c1)
entry_f2_c1.place(relx=0.15, rely=0.3)

entry_f2_c2 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f2_c2, entry_f2_c3)), "%S"), insertontime=0, textvariable=var_f2_c2)
entry_f2_c2.place(relx=0.3, rely=0.3)

entry_f2_c3 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f2_c3, entry_f2_c4)), "%S"), insertontime=0, textvariable=var_f2_c3)
entry_f2_c3.place(relx=0.45, rely=0.3)

entry_f2_c4 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f2_c4, entry_f2_c5)), "%S"), insertontime=0, textvariable=var_f2_c4)
entry_f2_c4.place(relx=0.6, rely=0.3)

entry_f2_c5 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f2_c5, labelWordle)), "%S"), insertontime=0, textvariable=var_f2_c5)
entry_f2_c5.place(relx=0.75, rely=0.3)

# ------------ fila 3 ------------

entry_f3_c1 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f3_c1, entry_f3_c2)), "%S"), insertontime=0, textvariable=var_f3_c1)
entry_f3_c1.place(relx=0.15, rely=0.4)

entry_f3_c2 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f3_c2, entry_f3_c3)), "%S"), insertontime=0, textvariable=var_f3_c2)
entry_f3_c2.place(relx=0.3, rely=0.4)

entry_f3_c3 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f3_c3, entry_f3_c4)), "%S"), insertontime=0, textvariable=var_f3_c3)
entry_f3_c3.place(relx=0.45, rely=0.4)

entry_f3_c4 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f3_c5, entry_f3_c5)), "%S"), insertontime=0, textvariable=var_f3_c4)
entry_f3_c4.place(relx=0.6, rely=0.4)

entry_f3_c5 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f3_c5, labelWordle)), "%S"), insertontime=0, textvariable=var_f3_c5)
entry_f3_c5.place(relx=0.75, rely=0.4)

# ------------ fila 4 ------------

entry_f4_c1 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f4_c1, entry_f4_c2)), "%S"), insertontime=0, textvariable=var_f4_c1)
entry_f4_c1.place(relx=0.15, rely=0.5)

entry_f4_c2 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f4_c2, entry_f4_c3)), "%S"), insertontime=0, textvariable=var_f4_c2)
entry_f4_c2.place(relx=0.3, rely=0.5)

entry_f4_c3 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f4_c3, entry_f4_c4)), "%S"), insertontime=0, textvariable=var_f4_c3)
entry_f4_c3.place(relx=0.45, rely=0.5)

entry_f4_c4 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f4_c4, entry_f4_c5)), "%S"), insertontime=0, textvariable=var_f4_c4)
entry_f4_c4.place(relx=0.6, rely=0.5)

entry_f4_c5 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f4_c5, labelWordle)), "%S"), insertontime=0, textvariable=var_f4_c5)
entry_f4_c5.place(relx=0.75, rely=0.5)

# ------------ fila 5 ------------

entry_f5_c1 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f5_c1, entry_f5_c2)), "%S"), insertontime=0, textvariable=var_f5_c1)
entry_f5_c1.place(relx=0.15, rely=0.6)

entry_f5_c2 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f5_c2, entry_f5_c3)), "%S"), insertontime=0, textvariable=var_f5_c2)
entry_f5_c2.place(relx=0.3, rely=0.6)

entry_f5_c3 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f5_c3, entry_f5_c4)), "%S"), insertontime=0, textvariable=var_f5_c3)
entry_f5_c3.place(relx=0.45, rely=0.6)

entry_f5_c4 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f5_c4, entry_f5_c5)), "%S"), insertontime=0, textvariable=var_f5_c4)
entry_f5_c4.place(relx=0.6, rely=0.6)

entry_f5_c5 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f5_c5, labelWordle)), "%S"), insertontime=0, textvariable=var_f5_c5)
entry_f5_c5.place(relx=0.75, rely=0.6)

# ------------ fila 6 ------------

entry_f6_c1 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f6_c1, entry_f6_c2)), "%S"), insertontime=0, textvariable=var_f6_c1)
entry_f6_c1.place(relx=0.15, rely=0.7)

entry_f6_c2 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f6_c2, entry_f6_c3)), "%S"), insertontime=0, textvariable=var_f6_c2)
entry_f6_c2.place(relx=0.3, rely=0.7)

entry_f6_c3 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f6_c3, entry_f6_c4)), "%S"), insertontime=0, textvariable=var_f6_c3)
entry_f6_c3.place(relx=0.45, rely=0.7)

entry_f6_c4 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f6_c4, entry_f6_c5)), "%S"), insertontime=0, textvariable=var_f6_c4)
entry_f6_c4.place(relx=0.6, rely=0.7)

entry_f6_c5 = CTkEntry(master=app, width=40, height=40, font=("Dubai", 20, "bold"), justify=CENTER, validate="key", validatecommand=(app.register(lambda event: validar_y_mover(event, entry_f6_c5, labelWordle)), "%S"), insertontime=0, textvariable=var_f6_c5)
entry_f6_c5.place(relx=0.75, rely=0.7)


# def mayus(*args):
#     todas_las_strvar = [var_f1_c1, var_f1_c2, var_f1_c3, var_f1_c4, var_f1_c5]
#     for y in todas_las_strvar:
#         letraMay = y.get()
#         letraMay = letraMay.upper()
#         y.set(letraMay)

# todas_las_strvar = [var_f1_c1, var_f1_c2, var_f1_c3, var_f1_c4, var_f1_c5]
# for y in todas_las_strvar:
#     y.trace("w", mayus)


entry_f1_c1.bind("<Key>", lambda event: borrar_y_mover(event, entry_f1_c1, entry_f1_c1))
entry_f1_c2.bind("<Key>", lambda event: borrar_y_mover(event, entry_f1_c2, entry_f1_c1))
entry_f1_c3.bind("<Key>", lambda event: borrar_y_mover(event, entry_f1_c3, entry_f1_c2))
entry_f1_c4.bind("<Key>", lambda event: borrar_y_mover(event, entry_f1_c4, entry_f1_c3))
entry_f1_c5.bind("<Key>", lambda event: borrar_y_mover(event, entry_f1_c5, entry_f1_c4))

entry_f2_c1.bind("<Key>", lambda event: borrar_y_mover(event, entry_f2_c1, entry_f2_c1))
entry_f2_c2.bind("<Key>", lambda event: borrar_y_mover(event, entry_f2_c2, entry_f2_c1))
entry_f2_c3.bind("<Key>", lambda event: borrar_y_mover(event, entry_f2_c3, entry_f2_c2))
entry_f2_c4.bind("<Key>", lambda event: borrar_y_mover(event, entry_f2_c4, entry_f2_c3))
entry_f2_c5.bind("<Key>", lambda event: borrar_y_mover(event, entry_f2_c5, entry_f2_c4))

entry_f3_c1.bind("<Key>", lambda event: borrar_y_mover(event, entry_f3_c1, entry_f3_c1))
entry_f3_c2.bind("<Key>", lambda event: borrar_y_mover(event, entry_f3_c2, entry_f3_c1))
entry_f3_c3.bind("<Key>", lambda event: borrar_y_mover(event, entry_f3_c3, entry_f3_c2))
entry_f3_c4.bind("<Key>", lambda event: borrar_y_mover(event, entry_f3_c4, entry_f3_c3))
entry_f3_c5.bind("<Key>", lambda event: borrar_y_mover(event, entry_f3_c5, entry_f3_c4))

entry_f4_c1.bind("<Key>", lambda event: borrar_y_mover(event, entry_f4_c1, entry_f4_c1))
entry_f4_c2.bind("<Key>", lambda event: borrar_y_mover(event, entry_f4_c2, entry_f4_c1))
entry_f4_c3.bind("<Key>", lambda event: borrar_y_mover(event, entry_f4_c3, entry_f4_c2))
entry_f4_c4.bind("<Key>", lambda event: borrar_y_mover(event, entry_f4_c4, entry_f4_c3))
entry_f4_c5.bind("<Key>", lambda event: borrar_y_mover(event, entry_f4_c5, entry_f4_c4))

entry_f5_c1.bind("<Key>", lambda event: borrar_y_mover(event, entry_f5_c1, entry_f5_c1))
entry_f5_c2.bind("<Key>", lambda event: borrar_y_mover(event, entry_f5_c2, entry_f5_c1))
entry_f5_c3.bind("<Key>", lambda event: borrar_y_mover(event, entry_f5_c3, entry_f5_c2))
entry_f5_c4.bind("<Key>", lambda event: borrar_y_mover(event, entry_f5_c4, entry_f5_c3))
entry_f5_c5.bind("<Key>", lambda event: borrar_y_mover(event, entry_f5_c5, entry_f5_c4))

entry_f6_c1.bind("<Key>", lambda event: borrar_y_mover(event, entry_f6_c1, entry_f6_c1))
entry_f6_c2.bind("<Key>", lambda event: borrar_y_mover(event, entry_f6_c2, entry_f6_c1))
entry_f6_c3.bind("<Key>", lambda event: borrar_y_mover(event, entry_f6_c3, entry_f6_c2))
entry_f6_c4.bind("<Key>", lambda event: borrar_y_mover(event, entry_f6_c4, entry_f6_c3))
entry_f6_c5.bind("<Key>", lambda event: borrar_y_mover(event, entry_f6_c5, entry_f6_c4))

labelWordle.bind("<Key>", lambda event: borrar_y_mover(event, labelWordle, labelWordle))
labelWordle.bind("<Key>", lambda event: enter(event, labelWordle, labelWordle, entry_f1_c1, entry_f1_c2, entry_f1_c3, entry_f1_c4, entry_f1_c5, entry_f2_c1, entry_f2_c2, entry_f2_c3, entry_f2_c4, entry_f2_c5, entry_f3_c1, entry_f3_c2, entry_f3_c3, entry_f3_c4, entry_f3_c5, entry_f4_c1, entry_f4_c2, entry_f4_c3, entry_f4_c4, entry_f4_c5, entry_f5_c1, entry_f5_c2, entry_f5_c3, entry_f5_c4, entry_f5_c5, entry_f6_c1, entry_f6_c2, entry_f6_c3, entry_f6_c4, entry_f6_c5, palabraElejida))



# ------------------------------------------------------------------------------------------------



# def elejirPalabraRandom():

miConexion = connect(r"C:\Users\MARTI\Desktop\PYTHON\BBDD\palabrasWordle")
miCursor = miConexion.cursor()
miCursor.execute("SELECT MAX(id) FROM PALABRAS")
global numeroPalabrasTotal
numeroPalabrasTotal = miCursor.fetchone()[0]

numPalabraElejida = random.choice(range(numeroPalabrasTotal))

miConexion = connect(r"C:\Users\MARTI\Desktop\PYTHON\BBDD\palabrasWordle")
miCursor = miConexion.cursor()
miCursor.execute("SELECT PALABRA FROM PALABRAS WHERE id=" + str(numPalabraElejida))

global palabraElejida
palabraElejida = miCursor.fetchone()
palabraElejida = palabraElejida[0]
print(palabraElejida)
    
miConexion.commit()
miConexion.close()



# def comprobarPalabra(entry_f1_c1, entry_f1_c2, entry_f1_c3, entry_f1_c4, entry_f1_c5, entry_f2_c1, entry_f2_c2, entry_f2_c3, entry_f2_c4, entry_f2_c5, entry_f3_c1, entry_f3_c2, entry_f3_c3, entry_f3_c4, entry_f3_c5, entry_f4_c1, entry_f4_c2, entry_f4_c3, entry_f4_c4, entry_f4_c5, entry_f5_c1, entry_f5_c2, entry_f5_c3, entry_f5_c4, entry_f5_c5, entry_f6_c1, entry_f6_c2, entry_f6_c3, entry_f6_c4, entry_f6_c5):
#     if entry_f1_c5.get() != "" and entry_f2_c5.get() == "" and entry_f3_c5.get() == "" and entry_f4_c5.get() == "" and entry_f5_c5.get() == "" and entry_f6_c5.get() == "":
#         paraulaUsuari = entry_f1_c1.get() + entry_f1_c2.get() + entry_f1_c3.get() + entry_f1_c4.get() + entry_f1_c5.get()

#     elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() == "" and entry_f4_c5.get() == "" and entry_f5_c5.get() == "" and entry_f6_c5.get() == "":
#         paraulaUsuari = entry_f2_c1.get() + entry_f2_c2.get() + entry_f3_c3.get() + entry_f4_c4.get() + entry_f5_c5.get()

#     elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() != "" and entry_f4_c5.get() == "" and entry_f5_c5.get() == "" and entry_f6_c5.get() == "":
#         paraulaUsuari = entry_f3_c1.get() + entry_f3_c2.get() + entry_f3_c3.get() + entry_f3_c4.get() + entry_f3_c5.get()

#     elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() != "" and entry_f4_c5.get() != "" and entry_f5_c5.get() == "" and entry_f6_c5.get() == "":
#         paraulaUsuari = entry_f4_c1.get() + entry_f4_c2.get() + entry_f4_c3.get() + entry_f4_c4.get() + entry_f4_c5.get()

#     elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() != "" and entry_f4_c5.get() != "" and entry_f5_c5.get() != "" and entry_f6_c5.get() == "":
#         paraulaUsuari = entry_f5_c1.get() + entry_f5_c2.get() + entry_f5_c3.get() + entry_f5_c4.get() + entry_f5_c5.get()

#     elif entry_f1_c5.get() != "" and entry_f2_c5.get() != "" and entry_f3_c5.get() != "" and entry_f4_c5.get() != "" and entry_f5_c5.get() != "" and entry_f6_c5.get() != "":
#         paraulaUsuari = entry_f6_c1.get() + entry_f6_c2.get() + entry_f6_c3.get() + entry_f6_c4.get() + entry_f6_c5.get()





root.mainloop()