# Importing tkinter module
# and all functions
from tkinter import *
from tkinter.ttk import *
from customtkinter import *

# creating master window
root = Tk()
app = CTkFrame(root)
app.pack(fill = BOTH, expand = 1)
# Entry widget
e1 = CTkEntry(app)
e1.focus_set()
e1.place(relx = 0.5, rely = 0.5, anchor = CENTER)


# Infinite loop
root.mainloop()
