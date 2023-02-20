import tkinter as tk
from tkinter import ttk

def callbackFunc(event):
     print("New Element Selected")
     lb.insert(1, "State")
     lb.insert(2, "Bird")
     lb.insert(3, "Flower")
     lb.insert(4, "Motto"
     lb.insert(5, "Nickname")
     lb.insert(6, "Date when joined Union)"
     if cb == "Alabama":
         lb2.insert(1,
         lb2.insert(1,
         lb2.insert(1,
         1b2.insert(1,



                     
r = tk.Tk() 
r.geometry('200x100')

labelTop = tk.Label(r,
                    text = "Choose your favourite month")
labelTop.grid(column=0, row=0)

cb=comboExample = ttk.Combobox(r, 
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

comboExample.bind("<<ComboboxSelected>>", callbackFunc)
lbox1 = tk.Listbox(r)
lbox.grid(row=4, column=1)
lbox2 = tk.Listbox(r)
lbox2.grid(row=4, column=2)               
r.mainloop()

##def callbackFunc(event):
##     print("New Element Selected")
##     if cb.get() == "Alabama"
##
##
##
##
##
##
##
##     
##     lb.insert(1, "State")
##     lb.insert(2, "Bird")
##     lb.insert(3, "Flower")
##     lb.insert(4, "Motto"
##     lb.insert(5, "Nickname")
##     lb.insert(6, "Date when joined Union)"
##     lb.insert(7, "State")
##     lb.insert(8, "State Bird"
##     lb.insert(9, "State")
##     lb.insert(10, "State Bird"
##     lb.insert(1, "State")
##     lb.insert(2, "State Bird"
##               
##     
##     
