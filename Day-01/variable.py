# ************* VARIABLE *************

# variable are named memory location which have reference to the value stored on
# unlike other programming languages python don't use any keyword to declare variables, just write the name of the variable and move on.

name = input("Enter your name : ")      # here we can see that input function which return name is assign to name named variable :p
print("Hello there " + name)            # Hello there <input_name>

# NOTE : Remember variable doesn't store any value, it has referenece to that value in memory, which on printing(calling) prints it




# A variable's value can be change at any given point in program within its scope.
name = "John Doe"
print("Hello there " + name)            # Hello there John Doe




# ************* Naming convention *************

# In python an identifier(name used for variables, function etc etc) should have proper name
# An identifier can contain (a-z), (A-Z), (0-9), ( _ )
# An identifier may have numbers in it but it can't start with it.
# Identifier with more than two words should be joined with _ . 
# An identifier should be as discriptive as the value or operation it is going to perform



# ####### Bad naming convention #######
# 1_name, first name, x

# ####### Good naming convention #######
# first_name, name2, age