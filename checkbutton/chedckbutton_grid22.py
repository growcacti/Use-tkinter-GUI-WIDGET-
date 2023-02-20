from tkinter import *

root = Tk()
root.geometry("300x200")

w = Label(root, text=" ", font="50")
w.grid(row=8, column=0)

chk1 = IntVar()
Checkbutton2 = IntVar()
Checkbutton3 = IntVar()

chkbtn1 = Checkbutton(
    root, text="   ", variable=C1, onvalue=1, offvalue=0, height=2, width=10
)

chkbtn2 = Checkbutton(
    root, text="", variable=Checkbutton2, onvalue=1, offvalue=0, height=2, width=10
)

chkbtn3 = Checkbutton(
    root, text="", variable=Checkbutton3, onvalue=1, offvalue=0, height=2, width=10
)

chkbtn1.grid(row=11, column=0)
chkbtn2.grid(row=13, column=0)
chkbtn3.grid(row=15, column=0)

mainloop()
