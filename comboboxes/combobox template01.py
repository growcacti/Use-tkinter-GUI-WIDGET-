import tkinter as tk
from tkinter import ttk


def callbackFunc(event):
    print("New Element Selected")


r = tk.Tk()
r.geometry("200x100")


def changeMonth():
    comboExample["values"] = ["July", "August", "September", "October"]


labelTop = tk.Label(r, text="Choose your favourite month")
labelTop.grid(column=0, row=0)

comboExample = ttk.Combobox(
    r, values=["January", "February", "March", "April"], postcommand=changeMonth
)


comboExample.grid(column=0, row=1)

r.mainloop()
