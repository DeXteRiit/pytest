import tkinter
import random


canvas = tkinter.Canvas(width=800, height=600)
canvas.pack()


class House:
    def __init__(self, canvas, x, y):
        self.canvas = canvas
        self.x = x
        self.y = y
        self.vx = 0
        self.vy = 0
        self.walls = self.canvas.create_rectangle(x, y, x + 50, y + 50)
        self.roof = self.canvas.create_line(x, y, x + 25, y - 50, x + 50, y)

    def move(self, vx, vy):
        self.canvas.move(self.walls, vx, vy)
        self.canvas.move(self.roof, vx, vy)
        self.canvas.update()
        self.canvas.after(100)


house = House(canvas, random.randint(100, 700), random.randint(100, 500))


def shoot(coords):
    x = coords.x
    y = coords.y
    canvas.create_oval(x + 10, y + 10, x - 10, y - 10, fill="black")


velocity = 10
#   while True:
#       house.move(velocity, 0)
#       canvas.after(100)


def move_up(event):
    house.move(0, -velocity)


def move_down(event):
    house.move(0, velocity)


def move_rigth(event):
    house.move(velocity, 0)


def move_left(event):
    house.move(-velocity, 0)


canvas.bind("<Button-1>", shoot)
canvas.bind_all("<w>", move_up)
canvas.bind_all("<s>", move_down)
canvas.bind_all("<d>", move_rigth)
canvas.bind_all("<a>", move_left)

canvas.mainloop()
