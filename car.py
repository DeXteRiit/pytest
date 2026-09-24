import tkinter

canvas = tkinter.Canvas(width=800, height=600)
canvas.pack()
canvas.create_rectangle(100, 50, 600, 250, fill="white")
canvas.create_oval(150, 200, 250, 300, fill="black")
canvas.create_oval(450, 200, 550, 300, fill="black")


canvas.mainloop()
