from tkinter import *
from tkinter import ttk

def clicked():
    message = "Textbox Value: " + txt.get()
    lbl.configure(text = message)


window = Tk()
window.title("BMI Chart")
window.geometry('500x500')

lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)

txt = Entry(window, width = 10)
txt.grid(column = 2, row = 0)

btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=3, row=0)

window.mainloop()
