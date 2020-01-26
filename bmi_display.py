from tkinter import *


from tkinter import messagebox


def enter_height():
    height = entry_1.get()

    label_2 = Label(root)
    label_2["text"] = height
    label_2.grid(row=4, column=1)


root = Tk()

label_1 = Label(root, text= "Height: ")
entry_1 = Entry(root)
button_1 = Button(root, text="Enter", command=enter_height());



label_1.grid(row=0, column=0)
entry_1.grid(row=0, column=1)
button_1.grid(row=1, column=0)





root.mainloop()

