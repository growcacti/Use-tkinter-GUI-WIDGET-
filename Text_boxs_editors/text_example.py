from tkinter import *

top = Tk()
text = Text(top)
text.insert(INSERT, "Georgia")
text.insert(END, "Brown Thrasher")
text.insert(END, "Live oak")
text.insert(END, "Nil sine numine")
text.insert(END, "January 2, 1788")

text.insert(END, "Salary.....")

text.pack()

top.mainloop()
