# ****************************
#            RANGE
# ****************************

# range() is the built in function which is used to generate range of numbers
# it have in total 3 parameters from which two are optional

'''
    SYNTAX : 

        range(initial_number, total_nums, increment_value)

        -> total_nums is the must parameter which is used to specify number we want generate, it will start
           from 0 by default and end at n-1 number cause last number is exclusive.
        -> if want to start from some given number we have to specify it before total_nums parameter/
        -> by default the increment process is done with count of 1, but with the help of third parameter we can
           customize it to
'''

nums = list(range(5))     # this will create range from 0 to 4
print(f"\n\nStarting from 0 upto 5 : {nums}")                   # Starting from 0 upto 5 : [0, 1, 2, 3, 4]

nums = list(range(1, 6))
print(f"Starting from 1 upto 6 : {nums}")                       # 

nums = list(range(1, 11, 2))
print(f"Starting from 1 upto 6 with increment of 2 : {nums}")
