import tkinter as tk
from tkinter import messagebox
import random

class HangmanGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Виселица")

        self.secret_word = self.choose_word()
        self.guessed_letters = []
        self.attempts = 6

        self.word_label = tk.Label(master, text=self.display_word())
        self.word_label.pack(pady=10)

        self.guess_entry = tk.Entry(master, width=3)
        self.guess_entry.pack(pady=10)

        self.guess_button = tk.Button(master, text="Угадать", command=self.make_guess)
        self.guess_button.pack()

    def choose_word(self):
        words = ["python", "programming", "hangman", "code", "challenge"]
        return random.choice(words)
    
    def display_word(self):
        display = ""
        for letter in self.secret_word:
            if letter in self.guessed_letters:
                display += letter
            else:
                display += "_"
        return display
    
    def make_guess(self):
        guess = self.guess_entry.get().lower()

        if len(guess) != 1 or not guess.isalpha():
            messagebox.showwarning("Предупреждение", "Пожалуйста, введите только одну букву.")
            return
        
        if guess in self.guessed_letters:
            messagebox.showwarning("Предупреждение", "Вы уже угадали эту букву. Попробуйте другую.")
            return
        
        self.guessed_letters.append(guess)

        if guess not in self.secret_word:
            self.attempts -= 1
            messagebox.showinfo("Неверно", f"Неверно! Осталось попыток: {self.attempts}")
            if self.attempts == 0:
                messagebox.showinfo("Игра окончена", f"Извините, вы проиграли. Загаданное слово было: {self.secret_word}")
                self.master.destroy()
            return
        
        # Переместите проверку победы сюда
        if set(self.guessed_letters) == set(self.secret_word):
            messagebox.showinfo("Поздравляю", f"Поздравляю, вы победили! Загаданное слово: {self.secret_word}")
            self.master.destroy()
            return

        self.word_label.config(text=self.display_word())

if __name__ == "__main__":
    root = tk.Tk()
    game = HangmanGame(root)
    root.mainloop()
