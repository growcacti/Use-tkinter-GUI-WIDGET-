import tkinter as tk
from tkinter import ttk

root = tk.Tk()


def details(event):
    print(event.widget)


combo1 = ttk.Combobox(root, name="box1")
combo1["values"] = ("A", "B", "C")
combo1.pack()
combo1.bind("<<ComboboxSelected>>", details)

combo2 = ttk.Combobox(root, name="box2")
combo2["values"] = ("D", "E", "F")
combo2.pack()
combo2.bind("<<ComboboxSelected>>", details)

root.mainloop()
