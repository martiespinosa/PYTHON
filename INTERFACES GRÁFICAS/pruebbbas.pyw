from tkinter import *

raiz = Tk()
raiz.config(bg = "red")

app = Frame()
app.config(bg = "grey", width = "810", height = "450")
app.pack(fill = "both", expand = "y")

etiq1 = Label(app, text = "ORANGE", font = ("", 120), bg = "grey")
etiq1.place(x = "50", y = "50")
etiq2 = Label(app, text = "is\nthe\nnew", font = ("MS Reference Sans Serif", 25), bg = "grey", justify = "left")
etiq2.place(x = "65", y = "240")
etiq3 = Label(app, text = "BLACK", font = ("", 120), bg = "grey", fg = "darkorange")
etiq3.place(x = "210", y = "210")

raiz.mainloop()