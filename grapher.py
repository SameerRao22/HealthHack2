from tkinter import *
from tkinter import ttk

def weightButton():




window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry("500x500")

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='First')
tab_control.add(tab2, text='Second')

weight_label = Label(tab1, text='Enter your Weight: ')
weight_label.grid(column=0, row=0)
weight_box = Entry(tab1, width = 10)
weight_box.grid(column = 1, row = 0)
# weight_button = Button(tab1, text = "Enter")
# weight_button.grid(column=2, row=0)

height_label = Label(tab1, text='Enter your Height: ')
height_label.grid(column=0, row=1)
height_box = Entry(tab1, width = 10)
height_box.grid(column = 1, row = 1)
# height_button = Button(tab1, text = "Enter")
# height_button.grid(column=2, row=1)

submit_button = Button(tab1, text = "Submit")


tab_control.pack(expand=1, fill='both')

window.mainloop()