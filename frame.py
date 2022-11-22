from tkinter import *
import tkinter as tk
from decimal import *


win = tk.Tk()
win.title("Калькулятор")
win.geometry("300x300+200+200")
win.grid_columnconfigure(3,minsize=40)
display = Entry(win,font=('Arial',16),width = 15)
display.insert(0,'0')
display.grid(row=0,column=0,columnspan=4,stick="we",padx=4,pady=2)
     
        








