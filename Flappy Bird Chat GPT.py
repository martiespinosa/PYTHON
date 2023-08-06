import tkinter as tk
import random

HEIGHT = 500
WIDTH = 800

def game_over():
    canvas.create_text(WIDTH / 2, HEIGHT / 2, text="Game Over!", font=("Helvetica", 30))
    bird.dead = True

def update_obstacles():
    for obstacle in obstacles:
        obstacle.move()
        if obstacle.check_collision(bird):
            game_over()
        if not obstacle.on_screen:
            obstacles.remove(obstacle)

def generate_obstacle():
    if len(obstacles) == 0 or obstacles[-1].x <= WIDTH * 0.8:
        y = random.randint(0, HEIGHT - 100)
        obstacles.append(Obstacle(canvas, WIDTH, y))

class Bird:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.id = canvas.create_rectangle(x - 10, y - 10, x + 10, y + 10, fill="red")
        self.canvas.move(self.id, WIDTH / 2, HEIGHT / 2)
        self.y = 0
        self.dead = False

    def jump(self):
        if not self.dead:
            self.y = -5

    def move(self):
        self.y += 0.5
        self.canvas.move(self.id, 0, self.y)
        pos = self.canvas.coords(self.id)
        if pos[3] >= HEIGHT or pos[1] <= 0:
            game_over()

class Obstacle:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.id = canvas.create_rectangle(0, y, 20, y + 100, fill="green")
        self.canvas.move(self.id, x, 0)
        self.on_screen = True

    def move(self):
        self.x -= 2
        self.canvas.move(self.id, -2, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] + 20 < 0:
            self.on_screen = False

    def check_collision(self, bird):
        bird_pos = bird.canvas.coords(bird.id)
        pos = self.canvas.coords(self.id)
        if pos[2] >= bird_pos[0] and pos[0] <= bird_pos[2]:
            if bird_pos[3] >= pos[1] and bird_pos[1] <= pos[3]:
                return True
        return False

root = tk.Tk()
root.title("Flappy Bird")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

bird = Bird(canvas, 0, 0)

obstacles = []

root.bind
