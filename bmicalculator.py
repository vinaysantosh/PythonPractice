# this program take height and weight as input and prints out the BMI

height = float(input("Enter your height in m : "))
weight = float(input ("Enter your weight in kg : "))

bmi = round(weight/(height**2))

print("Your BMI is: " + str(bmi))