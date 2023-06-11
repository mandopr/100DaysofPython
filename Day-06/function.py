# ****************************
#          FUNCTION
# ****************************

# A function is named code block
# function is used to wrap up block of code and use as many time as we want

'''
    SYNTAX : 

    def <function_name>() :
        """Some documentation regarding function"""
        code block ...

    1. here <def> indicated the defining of function followed by name of the function followed by braces (), for parameters (if there are)
    2. after that we end function header with :, which also represents start of function code block
    3. note that code block is body of function so it has to be indented

    -> The above procedure of function is known as function defination
    -> to actually execute function we need to call it


    SYNTAX : 

    <function_name>()
    -> To call the function we use function name followed by braces for passing arguments (if there are some) else it will be empty.
'''

def something():                # function defination
    ''' This function can print something '''
    print("\nSup, hehehehe")

something()                     # Sup, hehehehe





# ************* FUNCTION PARAMETERS AND ARGUMENTS *************

# function can perform certain task repeativly but it will be static.
# if we want function to do work dynamically, we want arguments and parameters


'''
    SYNTAX : 

    def <function_name>(parameter(s)):
        code block ...

    <function_name>(argument(s))

    1. through arguments, we can send data at function calling to function
    2. with parameters, function will access that data and store it (parameters are like temporary non-local variable)
    3. the order and type in which we pass values through arguments must be accessed by parameters accordingly, otherwise there will be conflict. 
'''

def greetings(name):
    print(f"Hello! {name}")

greetings("John")               # Hello! John





# ************* RETURN *************

# function can't just print something, it can return result as well.
# what makes return more usefull from print is that we can pass that value to some other functions, variables etc for further uses ...

'''
    SYNTAX : 

    def <function_name>():
        code block...
        return something

    <variable_name> = <function_name>()
'''

def add(num1, num2):
    return num1 + num2

result = add(6, 4)
print(result)




# ************* DEFAULT PARAMETERS *************

# default parameters can assign a default value to parameters when we somehow forget to gave value through arguments
def sub(num1, num2 = 0):
    return num1 - num2

result = sub(6)
print(result)




# ************* KEYWORD ARGUMENTS *************

# keyword argument unlike normal arguments don't have to get accessed by parameters in ordered way, there are names for each arguments
def fullname(firstname, lastname):
    return f"{firstname} {lastname}"

# here the order of arguments is not same as parameters
fullname(lastname="Uchiha", firstname="Shisui")     # Shisui Uchiha