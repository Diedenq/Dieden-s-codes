import tkinter as tk
import random

class PongGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Пинг-понг")

        self.canvas = tk.Canvas(master, width=400, height=300, bg="black")
        self.canvas.pack()

        self.paddle = self.canvas.create_rectangle(0, 150, 20, 250, fill="white")
        self.ball = self.canvas.create_oval(190, 140, 210, 160, fill="white")

        self.ball_speed = [3, 2]

        self.master.bind("<Up>", lambda event: self.move_paddle(-20))
        self.master.bind("<Down>", lambda event: self.move_paddle(20))

        self.update_game()

    def move_paddle(self, dy):
        current_coords = self.canvas.coords(self.paddle)
        if (current_coords[1] + dy >= 0) and (current_coords[3] + dy <= 300):
            self.canvas.move(self.paddle, 0, dy)

    def end_game(self):
        self.canvas.create_text(200, 150, text="Game Over", font=("Helvetica", 16), fill="white")
        self.master.after(2000, self.master.destroy)  # Close the window after 2000 milliseconds (2 seconds)

    def update_game(self):
        ball_coords = self.canvas.coords(self.ball)
        paddle_coords = self.canvas.coords(self.paddle)

        if ball_coords[0] <= 0:
            self.end_game()

        if ball_coords[2] >= 400:
            self.ball_speed[0] *= -1

        if ball_coords[1] <= 0 or ball_coords[3] >= 300:
            self.ball_speed[1] *= -1

        if (paddle_coords[0] < ball_coords[2] and paddle_coords[2] > ball_coords[0] and
                paddle_coords[1] < ball_coords[3] and paddle_coords[3] > ball_coords[1]):
            self.ball_speed[0] *= -1

        self.canvas.move(self.ball, self.ball_speed[0], self.ball_speed[1])

        self.master.after(16, self.update_game)

if __name__ == "__main__":
    root = tk.Tk()
    game = PongGame(root)
    root.mainloop()
