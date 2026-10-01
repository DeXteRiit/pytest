import random
import tkinter

targetX = 400
targetY = 400
canvas = tkinter.Canvas(width=2 * targetX, height=2 * targetY)
canvas.pack()
color = "black"

_ = canvas.create_line(0, targetY, 2 * targetX, targetY)
_ = canvas.create_line(targetX, 0, targetX, 2 * targetY)

for radius in range(targetY // 10, 11 // 10 * targetY, targetY // 10):
    _ = canvas.create_oval(
        targetX - radius, targetY - radius, targetX + radius, targetY + radius
    )


def shoot(x, y, color):

    if x == 400 and y == 400:
        color = "red"
        print("You win, you succesfully kirked him, you can finally take a rest")
    _ = canvas.create_oval(
        x - radius,
        y - radius,
        x + radius,
        y + radius,
        fill=color,
    )
    canvas.update()
    _ = canvas.after(200)


radius = 10
for circle in range(10000):
    shoot(random.randint(0, 2 * targetY), random.randint(0, 2 * targetY), color)


canvas.mainloop()
