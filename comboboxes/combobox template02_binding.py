import tkinter as tk
from tkinter import ttk


def callbackFunc(event):
    print("New Element Selected")


r = tk.Tk()
r.geometry("200x100")

labelTop = tk.Label(r, text="Choose your favourite month")
labelTop.grid(column=0, row=0)

comboExample = ttk.Combobox(
    r,
    values=[
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ],
)

comboExample.grid(column=0, row=1)
comboExample.current(1)

comboExample.bind("<<ComboboxSelected>>", callbackFunc)


r.mainloop()


def callbackFunc(event):
    print("New Element Selected")
