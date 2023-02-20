#!/usr/bin/env python
import pyautogui as pg
import pyperclip as pc
import tkinter as tk


root = tk.Tk()

keys = [
    "\u0394",
    "\u0393",
    "\u2111",
    "\u039b",
    "\u03a9",
    "\u03a6",
    "\u03a0",
]
curBut = [-1, -1]
buttonL = [[]]
varRow = 1
varColumn = 0


def select(value, x, y):
    if curBut != [-1, -1]:
        buttonL[curBut[0]][curBut[1]].configure(highlightbackground="#d9d9d9")
        buttonL[curBut[0]][curBut[1]].configure(highlightcolor="#d9d9d9")
    curBut[:] = [x, y]
    buttonL[x][y].configure(highlightbackground="red")
    buttonL[x][y].configure(highlightcolor="red")
    if value == "DEL":
        input_val = entry.get("1.0", "end-2c")
        entry.delete("1.0", "end")
        entry.insert("1.0", input_val, "end")
    elif value == "SPACE":
        entry.insert("insert", " ")
    elif value == "TAB":
        entry.insert("insert", "   ")
    else:
        entry.insert("end", value)


for button in keys:
    but = tk.Button(
        root,
        text=button,
        width=5,
        bg="light yellow",
        fg="black",
        highlightthickness=4,
        activebackground="cyan",
        highlightcolor="red",
        activeforeground="purple",
        relief="raised",
        padx=1,
        pady=1,
        bd=8,
        command=lambda x=button, i=varRow - 1, j=varColumn: select(x, i, j),
    )
    but.bind(
        "<Return>", lambda event, x=button, i=varRow - 1, j=varColumn: select(x, i, j)
    )
    buttonL[varRow - 1].append(but)
    but.grid(row=varRow, column=varColumn)
    varColumn += 1
    if varColumn > 20:
        varColumn = 0
        varRow += 1
        buttonL.append([])
