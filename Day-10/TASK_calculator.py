import os
from calculator_art import logo

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide
}

def calculator():
    os.system("cls")
    print(logo)
    num1 = float(input("\nEnter number-1 : "))

    should_continue = True
    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from above : ")
        num2 = float(input("Enter number-2 : "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")


        wanna_continue = input("Wanna continue? Types 'y' to continue or 'n' to start again or 'exit' to exit from the program : ")
        if wanna_continue == "y":
            os.system("cls")
            num1 = answer
        elif wanna_continue == "n":
            should_continue = False
            calculator()
        elif wanna_continue == "exit":
            should_continue = False
        else:
            print("Print valid option")

calculator()