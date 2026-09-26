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

radius = 10
for circle in range(10000):
    shotX = random.randint(0, 2 * targetX)
    shotY = random.randint(0, 2 * targetY)
    if shotX == 400 and shotY == 400:
        color = "red"
        print("You win, you succesfully kirked him, you can finally take a rest")
    _ = canvas.create_oval(
        shotX - radius,
        shotY - radius,
        shotX + radius,
        shotY + radius,
        fill=color,
    )
    canvas.update()
    canvas.after(100)
    color = "black"

canvas.mainloop()
