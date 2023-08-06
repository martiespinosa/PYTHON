import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora iPhone")
        
        self.total = tk.StringVar()
        self.total.set("0")
        
        self.entry = tk.Entry(master, textvariable=self.total, font=("Helvetica", 20))
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=5, ipady=10)
        
        self.create_buttons()
    
    def create_buttons(self):
        button_list = [
            ("7", self.callback),
            ("8", self.callback),
            ("9", self.callback),
            ("+", self.callback),
            ("4", self.callback),
            ("5", self.callback),
            ("6", self.callback),
            ("-", self.callback),
            ("1", self.callback),
            ("2", self.callback),
            ("3", self.callback),
            ("*", self.callback),
            ("0", self.callback),
            ("C", self.callback),
            ("=", self.callback),
            ("/", self.callback),
        ]
        
        row = 1
        col = 0
        for text, command in button_list:
            button = tk.Button(self.master, text=text, width=5, height=2, command=lambda: command(text))
            button.grid(row=row, column=col, padx=5, pady=5)
            
            col += 1
            if col > 3:
                col = 0
                row += 1
    
    def callback(self, text):
        current = self.total.get()
        if text == "C":
            self.total.set("0")
        elif text == "=":
            try:
                self.total.set(eval(current))
            except:
                self.total.set("Error")
        else:
            self.total.set(current + text)

root = tk.Tk()
calc = Calculator(root)
root.mainloop()