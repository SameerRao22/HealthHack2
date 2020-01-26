import matplotlib

import matplotlib.pyplot as plt
#x/y^2 = 18.5
#weight/heigth^2 = 19.5

def underweight(weight):
    height = (weight/18.5) ** 0.5
    return height

def normalweight(weight):
    height = (weight/25)** 0.5
    return height

def overweight(weight):
    height = (weight/30) ** 0.5
    return height



weight1 = []
height1 = []
weight2 = []
height2 = []
weight3 = []
height3 = []


for x in range(0, 301):
    weight1.append(x)

for x in range(0, 301):
    height1.append(underweight(x))

for x in range(0, 301):
    height2.append(normalweight(x))

for x in range(0, 301):
    height3.append(overweight(x))


#print(height)

#print(weight)


plt.plot(height1, weight1)
plt.plot(height2, weight1)
plt.plot(height3, weight1)



plt.ylabel('weight')
plt.xlabel('height')

plt.show()
