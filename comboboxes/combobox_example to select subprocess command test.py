import tkinter as tk
from tkinter import ttk

root = tk.Tk()
my_string_var = tk.StringVar()

combobox = ttk.Combobox(
    root,
    textvariable=my_string_var,
    values=["subprocess.run", "subprocess.Popen", "os.listdir()"],
)
combobox.grid(row=1, column=1)
root.mainloop()
