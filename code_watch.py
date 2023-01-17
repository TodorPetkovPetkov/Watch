from time import strftime
from tkinter import *
from tkinter.ttk import *

root = Tk()
root.title('SoftUni Basic Clock')


def clock():
    tick = strftime('%H:%M:%S %p')
    label.config(text=tick)
    label.after(1000, clock)


label = Label(root, font=('sans', 150), background='white', foreground='green')
label.pack(anchor="center")

clock()
mainloop()