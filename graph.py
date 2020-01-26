import matplotlib
import BMI_Class
import matplotlib.pyplot as plt

def underweight(weight):
    height = (weight/18.5) ** 0.5
    return height

def normalweight(weight):
    height = (weight/25)** 0.5
    return height

def overweight(weight):
    height = (weight/30) ** 0.5
    return height




def bmi_graph():
    weight1 = []
    height1 = []
    weight2 = []
    height2 = []
    weight3 = []
    height3 = []
    for x in range(0, 301):
        weight1.append(x*2.2)

    for x in range(0, 301):
        height1.append(underweight(x)*39.37)

    for x in range(0, 301):
        height2.append(normalweight(x)*39.37)

    for x in range(0, 301):
        height3.append(overweight(x)*39.37)
    plt.plot(height1, weight1)
    plt.plot(height2, weight1)
    plt.plot(height3, weight1)
    plt.suptitle('BMI chart', fontsize=16)

    plt.ylabel('weight(pounds)')
    plt.xlabel('height(inches)')


def my_bmi(height, weight):
    plt.plot(height, weight, 'r+')

def callgraph():
    plt.show()

