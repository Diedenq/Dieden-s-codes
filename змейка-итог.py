import tkinter as tk
import random

class SnakeGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Змейка")

        self.canvas = tk.Canvas(master, width=300, height=300, bg="black")
        self.canvas.pack()

        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.food = self.spawn_food()

        self.direction = "Right"

        self.master.bind("<Up>", lambda event: self.change_direction("Up"))
        self.master.bind("<Down>", lambda event: self.change_direction("Down"))
        self.master.bind("<Left>", lambda event: self.change_direction("Left"))
        self.master.bind("<Right>", lambda event: self.change_direction("Right"))

        self.after_id = None  # ID for scheduled update_game call

        self.update_game()

    def spawn_food(self):
        x = random.randint(1, 29) * 10
        y = random.randint(1, 29) * 10
        self.canvas.create_rectangle(x, y, x+10, y+10, fill="red", tags="food")
        return x, y

    def change_direction(self, new_direction):
        opposite_direction = {"Up": "Down", "Down": "Up", "Left": "Right", "Right": "Left"}
        if new_direction != opposite_direction[self.direction]:
            self.direction = new_direction

    def move(self):
        x, y = self.snake[0]
        if self.direction == "Up":
            y -= 10
        elif self.direction == "Down":
            y += 10
        elif self.direction == "Left":
            x -= 10
        elif self.direction == "Right":
            x += 10

        if not (0 <= x < 300 and 0 <= y < 300) or self.snake[0] in self.snake[1:]:
            self.game_over()
            return

        if (x, y) == self.food:
            self.canvas.delete("food")
            self.food = self.spawn_food()
            self.snake.insert(0, (x, y))
        else:
            self.snake.insert(0, (x, y))
            self.canvas.delete("snake")
            for segment in self.snake:
                x, y = segment
                self.canvas.create_rectangle(x, y, x + 10, y + 10, fill="green", tags="snake")
            self.snake.pop()

        self.check_collision()

    def check_collision(self):
        x, y = self.snake[0]
        if self.snake[0] in self.snake[1:]:
            self.game_over()

    def game_over(self):
        self.canvas.create_text(150, 150, text="Game Over\nClick to restart", fill="white", font=("Helvetica", 16), tags="game_over")
        self.canvas.bind("<Button-1>", self.reset_game)

    def reset_game(self, event):
        self.canvas.delete("snake")
        self.canvas.delete("food")
        self.canvas.delete("game_over")

        self.snake = [(100, 100), (90, 100), (80, 100)]
        self.food = self.spawn_food()
        self.direction = "Right"

        # Cancel all previous scheduled calls to update_game
        if self.after_id:
            self.master.after_cancel(self.after_id)

        # Start the game loop
        self.update_game()

    def update_game(self):
        self.move()
        
        # Schedule the next update_game call
        self.after_id = self.master.after(100, self.update_game)

if __name__ == "__main__":
    root = tk.Tk()
    game = SnakeGame(root)
    root.mainloop()