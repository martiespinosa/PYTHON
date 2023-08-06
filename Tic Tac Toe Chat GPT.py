import tkinter as tk

class TicTacToe(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)
        self.title("Tic Tac Toe")
        self.geometry("200x200")
        self.create_grid()
        self.turn = "X"

    def create_grid(self):
        self.buttons = {}
        for i in range(3):
            for j in range(3):
                b = tk.Button(self, text=" ", command=lambda row=i, col=j: self.play(row, col))
                b.grid(row=i, column=j)
                self.buttons[(i, j)] = b

    def play(self, row, col):
        button = self.buttons[(row, col)]
        if button["text"] == " ":
            button["text"] = self.turn
            if self.turn == "X":
                self.turn = "O"
            else:
                self.turn = "X"

    def run(self):
        self.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()