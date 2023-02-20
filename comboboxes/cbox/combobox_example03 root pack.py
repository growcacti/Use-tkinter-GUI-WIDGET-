import tkinter as tk
from tkinter import ttk

root = tk.Tk()
my_string_var = tk.StringVar()

combobox = ttk.Combobox(
    root,
    textvariable=my_string_var,
    values=[ "1. Aries\n",
        "2. Taurus\n",
        "3. Gemini\n",
        "4. Cancer\n",
        "5. Leo\n",
        "6. Virgo\n",
        "7. Libra\n",
        "8. Scorpio\n",
        "9. Sagittarius\n",
        "10. Capricorn\n",
        "11. Aquarius\n",
        "12. Pisces\n"]
)
combobox.pack()
root.mainloop()
