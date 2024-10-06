import streamlit

from tkinter import *
from tkinter.ttk import *
from time import strftime

root = Tk()
root.title("Clock by ZenithHexer")

def time():
    string = strftime('%H:%M:%S %p')
    label.config(text=string)
    label.after(1000, time)

label = Label(root, font=("Helvetica", 80), background="black", foreground="cyan")
label.pack(anchor='center')

time()

mainloop()
