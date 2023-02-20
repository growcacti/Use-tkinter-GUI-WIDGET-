import tkinter as tk

app = tk.Tk()
app.title("My App")
app.geometry("200x75")

frame = tk.Frame(app,bg="white",relief=tk.SUNKEN,bd=4)
frame.pack()

button = tk.Button(frame, text="Button")
button.pack()

entry = tk.Entry(frame)
entry.pack()

app.mainloop()

