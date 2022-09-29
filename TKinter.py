from tkinter import Tk,Label,Button, Entry
from xml.etree.ElementTree import Comment

window = Tk()
#spal to 😎
window.minsize(420,420)

#Label 1
lb1=Label(text="sus 1")
lb1.grid(column=0, row=1)

#Label 2
lb2=Label(text="sus 2")
lb2.grid(column=0, row=2)

#Button
btn = Button()
btn.config(text="przycisk")
btn.grid(column=0, row=3)

#Smoll button

#funkcja
def zmniejsz_przycisk():
    sizebutton["padx"] -= 1
    sizebutton["pady"] -= 1

sizebutton = Button()
sizebutton.config(text="smoll", command=zmniejsz_przycisk)
sizebutton.grid(column=0, row=4)
sizebutton.config(padx=40,pady=40)

#Entry
entry = Entry()
entry.grid(column=0, row=5)


window.mainloop()