from tkinter import *
from tkinter import messagebox
from tkinter import filedialog

root = Tk()
root.title("Prueba menús")
root.geometry("800x500")


def abrirfichero():
    fichero = filedialog.askopenfilename(title="Abrir", initialdir="C:", filetypes=(("Todos los ficheros", "*.*"), ("Fiheros Excel", "*.xlsx"), ("Ficheros Texto", "*.txt")))
    print(fichero)

def exit():
    valorExit = messagebox.askquestion("Exit", "¿Desea salir y cerrar la aplicacion?")
    if valorExit == "yes":
        root.destroy()



rowMenu = Menu(root)
root.config(menu = rowMenu)

fileMenu = Menu(rowMenu, tearoff=0)
fileMenu.add_command(label="Open File...", command=abrirfichero)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=exit)

editMenu = Menu(rowMenu, tearoff=0)
selectionMenu = Menu(rowMenu, tearoff=0)
viewMenu = Menu(rowMenu, tearoff=0)
goMenu = Menu(rowMenu, tearoff=0)
runMenu = Menu(rowMenu, tearoff=0)
terminalMenu = Menu(rowMenu, tearoff=0)
helpMenu = Menu(rowMenu, tearoff=0)

rowMenu.add_cascade(label="File", menu=fileMenu)
rowMenu.add_cascade(label="Edit", menu=editMenu)
rowMenu.add_cascade(label="Selection", menu=selectionMenu)
rowMenu.add_cascade(label="View", menu=viewMenu)
rowMenu.add_cascade(label="Go", menu=goMenu)
rowMenu.add_cascade(label="Run", menu=runMenu)
rowMenu.add_cascade(label="Terminal", menu=terminalMenu)
rowMenu.add_cascade(label="Help", menu=helpMenu)





root.mainloop()