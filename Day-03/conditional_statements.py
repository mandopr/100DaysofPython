# conditional statements are the piece of code, which decides program flow
'''
    there are many conditional statements like : 
    1. if
    2. if-else
    3. if-elif-else
    4. nested-if
'''





# ****************************
#             IF
# ****************************
# if statements runs a piece of code based on condition, IF the condition is true a piece of will get executed


# *********** IF SYNTAX ***********
'''
    if condition : (here : represents end of IF's header and start of IF's body)
        code block ... (NOTE : see here code block is indented which says its block of code)
'''

if 10 > 5:
    print("10 is greater than 5")





# ****************************
#           IF-ELSE
# ****************************
# what if we want to run some code when condition doesn't match, that's where else block will be used


# *********** IF-ELSE SYNTAX ***********
'''
    if condition : 
        code block ...
    else :  (here ELSE is on same indent as that of IF and ends with : which indicates start of ELSE's body)
        code block ...
'''

age = int(input("Enter your age : "))
if age > 18:
    print("You are eligible to drive")
else:
    print("You're not eligible to drive")





# ****************************
#         IF-ELIF-ELSE
# ****************************
# In the chunck of conditonal blocks what if we want extra condition to test, ELIF helps us here

# *********** IF-ELIF-ELSE SYNTAX ***********
'''
    if condition :
        code block ...
    elif condition :
        code block ...
    else :
        code block ... 
'''

num = int(input("Enter any whole number : "))
if num == 0:
    print("Its zero")
elif num % 2 == 0:
    print("Its even")
elif num % 2 != 0:
    print("Its odd")
else:
    print("Print somae valid whole numbers !!")





# ****************************
#         NESTED-IF
# ****************************
# we can use nested if to conditionarise our code more
# we can also perform else in nested if's

# *********** NESTED-IF SYNTAX ***********
'''
    if condition :
        if condition :
            code block ...
'''

height = int(input("Enter your height in cm : "))
weight = int(input("Enter your weight in kg : "))

if height < 190:
    if weight < 100:
        print("You can ride on roller coaster")    