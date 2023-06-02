# When we programmers work on big projects its better to split the big chunk of code into small modules
# A module can have some variables, functions, class in it which can be used multiple times across different files.

'''
    There are many built-in modules in python like : 
    
    Math
    Random
    etc etc ...
'''
# to use module we have to import the file/script via which we want to work with like below : 
import random

# we can also specify which function/variable/class we want to use from module like below :
from demo_mod import PI

# randint() is function in random module which generates random integers between specified numbers (inclusive)
print(f"\nrandint : {random.randint(1,10)}") 

# random() is function in random module which generates a random number between 0.0 - 1.0 but 1.0 is exclusive 
print(f"random : {random.random()}")
print(f"PI : {random.random()}")