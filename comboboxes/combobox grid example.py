import tkinter as tk
from tkinter import ttk

root = tk.Tk()
my_string_var = tk.StringVar()
var1 = tk.StringVar()
var2 = tk.StringVar()
var3 = tk.StringVar()


combobox = ttk.Combobox(
    root, textvariable=my_string_var, values=["Option 1", "Option 2", "Option 3"]
)
combobox.grid(row=1, column=1)


cb2 = ttk.Combobox(root, textvariable=var1, values=["Option 1", "Option 2", "Option 3"])

cb2.grid(row=1, column=2)


cb3 = ttk.Combobox(root, textvariable=var2, values=["Option 1", "Option 2", "Option 3"])

cb3.grid(row=1, column=3)


cb4 = ttk.Combobox(root, textvariable=var2, values=["Option 1", "Option 2", "Option 3"])
cb4.grid(row=1, column=4)


root.mainloop()
