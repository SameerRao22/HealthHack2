import matplotlib.pyplot as plt
class BMI_Class:
    BMI = float()
    BMI_values = []

    def add_BMI(self, weight, height):
        self.BMI = (weight/2.2) / ((height(2.54)/100)**2)
        self.BMI_values.append(self.BMI)


    def get_BMI(self):
        return self.BMI

    def get_Weight_Class(self):
        if self.BMI < 18.5:
            return "underweight"
        elif self.BMI < 25:
            return "healthy"
        elif self.BMI < 30:
            return "overweight"
        else:
            return "obese"

    def get_BMI_Vals(self):
        return self.BMI_values

    def graph_BMI(self):
        plt.plot(self.BMI_values)
        plt.xlabel('x-axis')
        plt.ylabel('y-axis')
        plt.title('BMI')
        plt.show()