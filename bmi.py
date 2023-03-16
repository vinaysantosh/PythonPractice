# this program takes as input the persons height and weight and tells if the person is overweight or underweight

height = float(input("Enter your height in m : "))
weight = float(input("Enter your weight in kg : "))

bmi = round(weight / (height ** 2))
print (f"Your bmi is {bmi} \n")
if (bmi <= 18.5):
    print("You are underweight")
elif (bmi>18.5 and bmi<=25):
    print("You have a normal weight")
elif (bmi>25 and bmi<=30):
    print("You are overweight")
elif (bmi>30 and bmi<=35):
    print("you are obese")
else:
    print("You are clinically obese")