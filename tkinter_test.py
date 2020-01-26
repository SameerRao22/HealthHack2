from tkinter import *

root = Tk()
topFrame = Frame(root)
topFrame.pack()

bottomFrame = Frame(root)
bottomFrame.pack(side = BOTTOM)

button1 = Button(topFrame, text = "button 1", fg = "red")
button2 = Button(topFrame, text = "button 2", fg = "green")
button3 = Button(topFrame, text = "button 3", fg = "blue")
button4 = Button(topFrame, text = "button 4", fg = "yellow")

label1 = Label(bottomFrame, text = "this is a textbox", bg = "yellow", fg = "")
label1.pack()

button1.pack(side = LEFT)
button2.pack(side = RIGHT)
button3.pack(side = TOP)
button4.pack(side = BOTTOM)


root.mainloop()