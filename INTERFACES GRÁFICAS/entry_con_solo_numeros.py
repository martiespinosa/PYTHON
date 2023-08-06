import tkinter as tk
 
validate_entry = lambda text: text.isdecimal()
 
root = tk.Tk()
root.config(width=300, height=200)
root.title("Mi aplicación")
 
entry = tk.Entry(
    validate="key",
    validatecommand=(root.register(validate_entry), "%S")
)
 
entry.place(x=50, y=50, width=150)
root.mainloop()