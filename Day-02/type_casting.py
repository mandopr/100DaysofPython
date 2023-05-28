# ************* TYPE CASTING *************

# Type casting can be done in two ways : 
# 1. implicitly -> in some part of code there would be type casting which even we developers don't know like on changing data in variable
#                   datatype of variable changes implicitly
# 2. explicitly -> explicitly type casting is what we developers do forcefully by built-in methods



age = input("What's your age : ")
print(age, type(age))           # <inputed age> <class 'str'>

# here by default input function takes input in string format, even we have written number it will be returned as string
# so we need to use type casting which means changing datatypes
# type casting can be done with the help of python built-in functions like str(), int(), float(), bool()
# now we can change type of age with int() to integer
print(type((int(age))))           # <inputed age> <class 'int'>



# TASKS
print('12' + '34')  # 1234  -> These are not normal numbers, they are actually numbers surroundedv by quotes, WTF! they are string !!?

# we can type cast them and then add them
print(int('12') + int('34'))            # 46