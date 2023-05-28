# taking height from user via input and converting it into float
height = float(input("Enter your height in m : "))
# taking weight from user via input and converting it into float
weight = float(input("Enter your weight in kg : "))

# BMI formula
bmi = weight/(height**2)
print(f"Your bmi is : " + str(bmi))