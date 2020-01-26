from tkinter import *
from tkinter import ttk
from BMI_Class import BMI_Class
from tkinter import messagebox

def SubmitClicked():
    weightNum =  float(weight_box.get())
    heightNum = float(height_box.get())
    BMI_Chart.add_BMI(weightNum, heightNum)
    bmi_label.configure(text = str(BMI_Chart.BMI))
    messagebox.showinfo('BMI CHART', "Your BMI was successfully calculated\n If you want to see the graph switch to tab 2 or enter more values")

window = Tk()
window.title("BMI Chart")
window.geometry("500x500")

BMI_Chart = BMI_Class()

tab_control = ttk.Notebook(window)
tab1 = ttk.Frame(tab_control)
tab2 = ttk.Frame(tab_control)

tab_control.add(tab1, text='Input')
tab_control.add(tab2, text='Graph')

weight_label = Label(tab1, text='Enter your Weight(LBS): ')
weight_label.grid(column=0, row=0)
weight_box = Entry(tab1, width = 10)
weight_box.grid(column = 1, row = 0)


height_label = Label(tab1, text='Enter your Height(IN): ')
height_label.grid(column=0, row=1)
height_box = Entry(tab1, width = 10)
height_box.grid(column = 1, row = 1)

submit_button = Button(tab1, text = "Submit", command = SubmitClicked)
submit_button.grid(column = 0, row = 4)

bmi_label = Label(tab1, text = "BMI: ")
bmi_label.grid(column = 0, row = 5)

graph_generator = Button(tab2, text = "Generate Graph")
graph_generator.grid(column = 0, row = 0)

tab_control.pack(expand=1, fill='both')
window.mainloop()
