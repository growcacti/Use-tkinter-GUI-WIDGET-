from tkinter import *

# from tkinter import messagebox

# creating root window
root = Tk()

# function_definitions
def callback():
    text = textEditor.get(0.1, END)
    print(text)


# defining text editor
textEditor = Text(
    root,
    width=43,
    height=10,
    font=(("Times"), 10, "bold"),
    wrap=WORD,
    fg="white",
    bg="black",
)
textEditor.pack()

# button 1
button1 = Button(root, text="Display Text", command=callback)
button1.pack(pady=12)

root.geometry("350x218")
root.title("PythonLobby")
root.mainloop()
