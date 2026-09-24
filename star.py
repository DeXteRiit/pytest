import tkinter

canvas = tkinter.Canvas(width=800, height=600)
canvas.pack()


hviezda = [
    200,
    50,
    240,
    150,
    350,
    150,
    260,
    220,
    300,
    330,
    200,
    260,
    100,
    330,
    140,
    220,
    50,
    150,
    160,
    150,
]
# canvas.create_polygon(10, 200, 100, 200, 100, 100, fill='red', width=2)
# canvas.create_polygon(hviezda, fill='red', width=2)
canvas.create_rectangle(10, 10, 800, 500, fill="white")


# canvas.create_polygon(hviezda, fill='yellow', outline='black')
canvas.create_oval(295, 145, 495, 345, fill="red")
canvas.create_text(350, 50, text="text")

canvas.mainloop()
