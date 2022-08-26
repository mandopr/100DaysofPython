# ****************************
#    ASSIGNMENT-OPERATORS
# ****************************
# assignment operators are used to assign a value after certain operation

'''
    Type of assignment operators : 

    =       ->      x = y                               ->      assignment operator
    +=      ->      x += y      ->      x = x + y       ->      addition assignment operator
    -=      ->      x-=y        ->      x = x - y       ->      subtraction assignment
    *=      ->      x*=y        ->      x = x * y       ->      multiplication assignment
    /=      ->      x/=y        ->      x = x / y       ->      division assignment
    **=     ->      x**=y       ->      x = x ** y      ->      power to assignment
'''

x = 5
y = 0

y = x
print(f"x , y -> {x,y}")

x += y
print(f"x , y -> {x,y}")

x -= y
print(f"x , y -> {x,y}")

x *= y
print(f"x , y -> {x,y}")

x /= y
print(f"x , y -> {x,y}")

x **= y
print(f"x , y -> {x,y}")