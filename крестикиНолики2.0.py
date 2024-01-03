import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self, master):
        self.master = master
        self.master.title("Крестики-нолики")
        self.current_player = "X"

        self.buttons = [[None, None, None],
                        [None, None, None],
                        [None, None, None]]
        
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.master, text="", font=('normal', 20), width=5, height=2,
                                               command=lambda row=i, col=j: self.on_click(row, col))
                self.buttons[i][j].grid(row=i, column=j)
    
    def on_click(self, row, col):
        if not self.buttons[row][col]['text']:
            self.buttons[row][col]['text'] = self.current_player
            if self.check_winner(row, col):
                messagebox.showinfo("Победа!", f"Игрок {self.current_player} победил!")
                self.reset_game()
            elif self.check_draw():
                messagebox.showinfo("Ничья!", "Ничья! Начните новую игру.")
                self.reset_game()
            else:
                self.switch_player()

    def check_winner(self, row, col):
        if all(self.buttons[row][i]['text'] == self.current_player for i in range(3)):
            return True
        if all(self.buttons[i][col]['text'] == self.current_player for i in range(3)):
            return True
        
        if row == col and all(self.buttons[i][i]['text'] == self.current_player for i in range(3)):
            return True
        if row + col == 2 and all(self.buttons[i][2 - i]['text'] == self.current_player for i in range(3)):
            return True
        return False
    
    def check_draw(self):
        return all(self.buttons[i][j]['text'] for i in range(3) for j in range(3))
    
    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j]['text'] = ""
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    game = TicTacToe(root)
    root.mainloop()
