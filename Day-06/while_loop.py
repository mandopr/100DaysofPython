# ****************************
#        WHILE LOOP
# ****************************

# while loop unlike for loops don't loop for limited amount of iteration, but they iterate uptill certain condition is False

'''
    SYNTAX : 

    while <condition>:
        code block...

    
    1. while is keyword used to refer as starting of while loop followed by condition, based on which loop will iterate if it is True
    2. followed by : which indicated end of while loop condition portion and start of code block of while loop.
'''

count = 1

while count <= 10:
    print(count)
    count += 1