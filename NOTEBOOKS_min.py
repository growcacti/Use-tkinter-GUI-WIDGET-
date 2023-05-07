
import tkinter as tk
#!/usr/bin/env python3
import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as mb
from tkinter.filedialog import askopenfilename, asksaveasfilename, askdirectory
from tkinter import filedialog
from tkinter import Tk, Frame, Button, BOTH, SUNKEN
from tkinter.colorchooser import askcolor
import os, sys, subprocess

import pyautogui as pag
import pyperclip as pc
import runpy
import glob
import time


from tkinter.scrolledtext import ScrolledText 

from NB1 import *
from NB2 import *
from NB3 import *
from frwidget import *
from codestrings import *

class LbTx(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.path = os.getcwd()
        self.parent = parent
        self.notebook = ttk.Notebook(self.parent)
        self.notebook.grid(row=0, column=0)
        self.f1 = ttk.Frame(self.notebook, width=1900, height=1080)
        self.f1.grid(row=0, column=1)
       
        self.notebook.add(self.f1, text="TAB1")
        self.f2 = ttk.Frame(self.notebook)
        self.notebook.add(self.f2, text='2')
                       
                      #################################################################Frame 3################################################################
        self.f3 = ttk.Frame(self.notebook)
        self.notebook.add(self.f3, text='3')
     
        #################################################################################################################################################

        self.f4 = ttk.Frame(self.notebook)
        self.notebook.add(self.f4, text='4')
     

              ########################################################################################
        self.f5 = ttk.Frame(self.notebook)
        self.notebook.add(self.f5, text='5')
       


        ########################################################################################





        f6 = ttk.Frame(self.notebook)
        self.notebook.add(f6, text='6')
      


        ########################################################################################





        f7 = ttk.Frame(self.notebook)
        self.notebook.add(f7, text='7')
        


        ########################################################################################



        f8 = ttk.Frame(self.notebook)
        self.notebook.add(f8, text='8')
        

  


        ########################################################################################
        f9 = ttk.Frame(self.notebook)
        self.notebook.add(f9, text='9')
      
    
            
        ########################################################################################




        f10 = ttk.Frame(self.notebook)
        self.notebook.add(f10, text='10')
    
        ########################################################################################
        f11 = ttk.Frame(self.notebook)
        self.notebook.add(f11, text='11')
        
       


        ########################################################################################


        f12 = ttk.Frame(self.notebook)
        self.notebook.add(f12, text='12')
        
      


        ########################################################################################

        f13 = ttk.Frame(self.notebook)
        self.notebook.add(f13, text='13')
       
        

        f14 = ttk.Frame(self.notebook)
        self.notebook.add(f14, text='14')
        

        f15 = ttk.Frame(self.notebook)
        self.notebook.add(f15, text='15')
       
      

         

        f16 = ttk.Frame(self.notebook)
        self.notebook.add(f16, text='16')
        self.txt16 = ScrolledText(f16, height=1212, width=120)


        f17 = ttk.Frame(self.notebook)
        self.notebook.add(f17, text='17')
      

      


        

        f18 = ttk.Frame(self.notebook)
        self.notebook.add(f18, text='18')
        


        f19 = ttk.Frame(self.notebook)
        self.notebook.add(f19, text='19')
        

      

        f20 = ttk.Frame(self.notebook)
        self.notebook.add(f20, text='20')
       
        
        f21 = ttk.Frame(self.notebook)
        self.notebook.add(f21, text='201')
       

        f22 = ttk.Frame(self.notebook)
        self.notebook.add(f22, text='212')
      

        f23 = ttk.Frame(self.notebook)
        self.notebook.add(f23, text='220')
       
        f24 = ttk.Frame(self.notebook)
        self.notebook.add(f24, text='240')


      
def main():
    parent = tk.Tk()
    app=LbTx(parent)
    parent.mainloop()


if __name__== '__main__':
    main()
