import tkinter as tk
from tkinter import ttk

def callbackFunc(event):
     print("New Element Selected")
     
r = tk.Tk() 
r.geometry('200x100')

labelTop = tk.Label(r,
                    text = "Choose your favourite month")
labelTop.grid(column=0, row=0)
text = tk.Text(r)
cb = ttk.Combobox(r, 
                            values=[
                                    "Alabama",
                                    "Alaska",
                                    "Arizona",
                                    "Arkansas",
                                    "California",
                                    "Colorado",
                                    "Connecticut",
                                    "Delaware",
                                    "Florida",
                                    "Georgia",
                                    "Hawaii",
                                    "Idaho",
                                    "Illinois",
                                    "Indiana",
                                    "Iowa",
                                    "Kansas",
                                    "Kentucky",
                                    "Louisiana",
                                    "Maine",
                                    "Maryland",
                                    "Massachusetts",
                                    "Michigan",
                                    "Minnesota",
                                    "Mississippi",
                                    "Missouri",
                                    "Montana",
                                    "Nebraska",
                                    "Nevada",
                                    "New Hampshire",
                                    "New Jersey",
                                    "New Mexico",
                                    "New York",
                                    "North Carolina",
                                    "North Dakota",
                                    "Ohio",
                                    "Oklahoma",
                                    "Oregon",
                                    "Pennsylvania",
                                    "Rhode Island",
                                    "South Carolina",
                                    "South Dakota",
                                    "Tennessee",
                                    "Texas",
                                    "Utah",
                                    "Vermont",
                                    "Virginia",
                                    "Washington",
                                    "West Virginia",
                                    "Wisconsin"])
                            
                            

                                   
                                                                   
cb.grid(column=0, row=1)
cb.current(1)

cb.bind("<<ComboboxSelected>>", callbackFunc)


r.mainloop()

def callbackFunc(event):
     print("New Element Selected")
	 if cb == "Alabama""	
	 AL = {["Yellowhammer", "Longleaf pine","	"Audemus jura nostra defendere",	""December 14, 1819"]}
     text.insert(END, AL)
