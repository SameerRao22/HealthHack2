import matplotlib.pyplot as plt
import numpy as np
class BMI_Class:
    weight_values = []
    height_values = []
    BMI_Values = []

    def add_BMI(self, weight, height):
        self.weight_values.append(weight)
        self.height_values.append(height)
        self.BMI_Values.append((weight/2.2)/(((height*2.54)/100)**2))

    def get_Weight_Class(self):
        if self.BMI < 18.5:
            return "underweight"
        elif self.BMI < 25:
            return "healthy"
        elif self.BMI < 30:
            return "overweight"
        else:
            return "obese"

    def graph_BMI(self):
        plt.plot(self.weight_values, self.BMI_Values)
        plt.xlabel('weight')
        plt.ylabel('BMI Values')
        plt.title('BMI')
        plt.show()