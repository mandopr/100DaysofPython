print('''\n\n--------------------------------------------------
        \tBMI calculator!
--------------------------------------------------''')
# taking height from user via input and converting it into float
height = float(input("\nEnter your height in m : "))
# taking weight from user via input and converting it into float
weight = float(input("Enter your weight in kg : "))

# BMI formula
bmi = weight/(height**2)
print(f"\nYour bmi is : " + str(bmi))

if bmi < 18.5:
    print(f"\nYour BMI : {bmi}, you are underweight")
elif bmi>=18.5 and bmi<25:
    print(f"\nYour BMI : {bmi}, you have normal weight")
elif bmi>=25 and bmi<30:
    print(f"\nYour BMI : {bmi}, you are overweight")
elif bmi>=30 and bmi<35:
    print(f"\nYour BMI : {bmi}, you are obese")
else:
    print(f"\nYour BMI : {bmi}, you are clinically obese")