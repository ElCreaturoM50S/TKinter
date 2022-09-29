from distutils.command.config import config
from tkinter import Tk,Label,Button, Entry

window = Tk()
#spal to 😎
window.minsize(420,420)

lb1=Label(text="sus 1")
lb1.grid(column=0, row=1)

lb2=Label(text="sus 2")
lb2.grid(column=0, row=2)

btn = Button()
btn.config(text="przycisk")
btn.grid(column=0, row=3)

window.mainloop()