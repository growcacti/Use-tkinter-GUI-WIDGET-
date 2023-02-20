import tkinter as tk
from tkinter import Canvas

app = tk.Tk()
app.title("My App")
app.geometry("200x75")

canvas = Canvas(app)
canvas.create_line(10, 10, 150, 50)
canvas.pack()

app.mainloop()
