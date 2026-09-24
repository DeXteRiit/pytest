import random
import tkinter

canvas = tkinter.Canvas(height=600, width=800)
canvas.pack()
max_velocity = random.randrange(40, 80, 10)
x = random.randrange(100, 600)
# y = random.randrange(100, 400)
y = 200
size = 100
sizeRed = 17 / 20 * size
canvas.create_oval(
    x - size,
    y - size,
    x + size,
    y + size,
    fill="white",
    outline="black",
    width=size / 50,
)
canvas.create_oval(
    x - sizeRed,
    y - sizeRed,
    x + sizeRed,
    y + sizeRed,
    outline="red",
    width=size / 5,
)
canvas.create_text(x, y, text=max_velocity, font=("arial", size - 10, "bold"))

canvas.mainloop()
