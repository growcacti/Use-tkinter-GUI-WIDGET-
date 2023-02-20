from tkinter import *

root = Tk()
root.geometry("300x800")

w = Label(root, text=" ", font="50")
w.grid(row=8, column=0)


chk1 = IntVar()
chk2 = IntVar()
chk3 = IntVar()
chk4 = IntVar()
chk5 = IntVar()
chk6 = IntVar()
chk7 = IntVar()
chk8 = IntVar()
chk9 = IntVar()
chk10 = IntVar()

chkbtn1 = Checkbutton(
    root, text="   ", variable=chk1, onvalue=1, offvalue=0, height=2, width=10
)

chkbtn2 = Checkbutton(
    root, text="   ", variable=chk2, onvalue=1, offvalue=0, height=2, width=10
)

chkbtn3 = Checkbutton(
    root, text="   ", variable=chk3, onvalue=1, offvalue=0, height=2, width=10
)


chkbtn4 = Checkbutton(
    root, text="   ", variable=chk4, onvalue=1, offvalue=0, height=2, width=10
)
chkbtn5 = Checkbutton(
    root, text="   ", variable=chk5, onvalue=1, offvalue=0, height=2, width=10
)
chkbtn6 = Checkbutton(
    root, text="   ", variable=chk6, onvalue=1, offvalue=0, height=2, width=10
)
chkbtn7 = Checkbutton(
    root, text="   ", variable=chk7, onvalue=1, offvalue=0, height=2, width=10
)
chkbtn8 = Checkbutton(
    root, text="   ", variable=chk8, onvalue=1, offvalue=0, height=2, width=10
)
chkbtn9 = Checkbutton(
    root, text="   ", variable=chk9, onvalue=1, offvalue=0, height=2, width=10
)
chkbtn10 = Checkbutton(
    root, text="   ", variable=chk10, onvalue=1, offvalue=0, height=2, width=10
)


w = Label(root, text=" Title 1 ", font="50")
w.grid(row=0, column=0)

aa = Label(root, text=" Title 2 ", font="50")
aa.grid(row=0, column=1)

bb = Label(root, text=" Title 3", font="50")
bb.grid(row=0, column=2)

cc = Label(root, text="Title 4 ", font="50")
cc.grid(row=0, column=3)


chkbtn1.grid(row=1, column=3)
chkbtn2.grid(row=2, column=3)
chkbtn3.grid(row=3, column=3)

chkbtn4.grid(row=4, column=3)
chkbtn5.grid(row=5, column=3)
chkbtn6.grid(row=6, column=3)
chkbtn7.grid(row=7, column=3)
chkbtn8.grid(row=8, column=3)
chkbtn9.grid(row=9, column=3)
chkbtn10.grid(row=10, column=3)


root.mainloop()
