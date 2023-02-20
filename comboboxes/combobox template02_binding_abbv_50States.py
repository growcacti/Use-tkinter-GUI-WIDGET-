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
        "AL",
        "AK",
        "AZ",
        "AR",
        "CA",
        "CO",
        "CT",
        "DE",
        "FL",
        "GA",
        "HI",
        "ID",
        "IL",
        "IN",
        "IA",
        "KS",
        "KY",
        "LA",
        "ME",
        "MD",
        "MA",
        "MI",
        "MN",
        "MS",
        "MO",
        "MT",
        "NE",
        "NV",
        "NH",
        "NJ",
        "NM",
        "NY",
        "NC",
        "ND",
        "OH",
        "OK",
        "OR",
        "PA",
        "RI",
        "SC",
        "SD",
        "TN",
        "TX",
        "UT",
        "VT",
        "VA",
        "WA",
        "WV",
        "WI",
        "WY",
    ],
)
comboExample.grid(column=0, row=1)
comboExample.current(1)

comboExample.bind("<<ComboboxSelected>>", callbackFunc)


r.mainloop()


def callbackFunc(event):
    print("New Element Selected")
