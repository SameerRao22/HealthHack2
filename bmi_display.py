from tkinter import *
from tkinter import ttk
from BMI_Class import BMI_Class
from tkinter import messagebox
import graph

def SubmitClicked():
    global weightNum
    global heightNum
    weightNum = float(weight_box.get())
    heightNum = float(height_box.get())
    BMI_Chart.add_BMI(weightNum, heightNum)
    bmi_label.configure(text = 'BMI: '+str(BMI_Chart.BMI))
    new_weight_num = weightNum/2.2
    new_height_num = heightNum * 0.0254
    #weight/height^2 = 18.5

    if (BMI_Chart.BMI < 18.5):
        message = "You are underweight."
        ideal_weight = 18.5 * new_height_num**2
    elif (BMI_Chart.BMI < 25):
        message = "normal weight."
        ideal_weight = "You're weight is ideal."
    elif (BMI_Chart.BMI < 30):
        message = "You are overweight"
        ideal_weight = 18.5 * new_height_num ** 2
    else:
        message = "You are obese."
        ideal_weight = 18.5 * new_height_num ** 2
    weight_class_label.configure(text = message)
    ideal_weight_label.configure(text = 'Target weight: '+ str(round(ideal_weight*2.2, 1)) + "pounds")
    messagebox.showinfo('BMI CHART', "Your BMI was successfully calculated\n If you want to see the graph switch to tab 2 and click generate graph")


def GenerateGraph():
    graph.bmi_graph()
    graph.my_bmi(heightNum, weightNum)
    graph.callgraph()

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

graph_generator = Button(tab2, text = "Generate Graph", command = GenerateGraph)
graph_generator.grid(column = 0, row = 0)

weight_class_label = Label(tab1, text = 'weight class')
weight_class_label.grid(column = 0, row = 6)

ideal_weight_label = Label(tab1, text = 'Ideal Weight: ')
ideal_weight_label.grid(column = 0, row = 15)


tab_control.pack(expand=1, fill='both')
window.mainloop()