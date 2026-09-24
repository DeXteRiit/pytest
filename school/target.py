import tkinter
import random

x = 400
y = 400
canvas = tkinter.Canvas(width=2 * x, height=2 * y)
canvas.pack()
color = "black"

canvas.create_line(0, y, 2 * x, y)
canvas.create_line(x, 0, x, 2 * y)

for radius in range(int(y / 10), int(11 / 10 * y), int(y / 10)):
    canvas.create_oval(x - radius, y - radius, x + radius, y + radius)

radius = 10
for circle in range(10000):
    centerX = random.randint(0, 2 * x)
    centerY = random.randint(0, 2 * y)
    if centerX == 400 and centerY == 400:
        color = "red"
        print("You win, you succesfully kirked him, you can finally take a rest")
    canvas.create_oval(
        centerX - radius,
        centerY - radius,
        centerX + radius,
        centerY + radius,
        fill=color,
    )
    canvas.update()
    canvas.after(100)
    color = "black"

canvas.mainloop()
