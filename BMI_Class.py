from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk
from tkinter import *

class BMI_Class:
    BMI = float()
    weight_values = []
    height_values = []
    BMI_Values = []

    def add_BMI(self, weight, height):
        self.weight_values.append(weight)
        self.height_values.append(height)
        self.BMI = (weight/2.2)/(((height*2.54)/100)**2)
        self.BMI_Values.append(self.BMI)

    def get_Weight_Class(self):
        if self.BMI < 18.5:
            return "underweight"
        elif self.BMI < 25:
            return "healthy"
        elif self.BMI < 30:
            return "overweight"
        else:
            return "obese"

    def get_BMI_Values(self):
        return self.BMI_Values

    def graph_BMI(self):
        window = Tk()
        window.title("BMI Chart")
        window.geometry("500x500")
        f = Figure(figsize=(5, 5), dpi=100)
        a = f.add_subplot(111)
        a.plot([1, 2, 3, 4, 5, 6, 7, 8], [5, 6, 1, 3, 8, 9, 3, 5])

        canvas = FigureCanvasTkAgg(f, window)
        canvas.draw()
        canvas.get_tk_widget().pack(side=BOTTOM, fill=BOTH, expand=True)
        toolbar = NavigationToolbar2Tk(canvas, window)
        toolbar.update()
        canvas._tkcanvas.pack()

        window.mainloop()