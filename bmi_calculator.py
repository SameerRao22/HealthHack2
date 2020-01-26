def weight_converter(patient_weight):
    patient_weight = weight / 2.2
    return patient_weight

def height_converter(patient_height):
    patient_height = (height * 2.54) / 100
    return patient_height

def bmi_calculator(patient_weight, patient_height):
    patient_bmi = patient_weight / (patient_height ** 2)
    return patient_bmi

def bmi_range(my_bmi):
    a = 0
    if my_bmi < 18.5:
        weight_class = "underweight"
    elif my_bmi < 25:
        weight_class = "healthy"
        a = 1
    elif my_bmi < 30:
        weight_class = "overweight"
    else:
        weight_class = "obese"
    return weight_class

weight = int(input("Enter your weight(pounds): "))
height = int(input("Enter your height(inches): "))

final_weight = weight_converter(weight)
final_height = height_converter(height)
bmi = bmi_calculator(final_weight, final_height)
bmi_class = bmi_range(bmi)

print("Your BMI is ", bmi)
if bmi_class == "healthy":
    print("You have a healthy bodyweight.")
else:
    print("You are " + bmi_class)







