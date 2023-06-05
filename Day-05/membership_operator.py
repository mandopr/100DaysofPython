# ****************************
#     MEMBERSHIP OPERATOR
# ****************************

# membership operators are used to look out for the element, that whether it is present in specified sequence.
'''
    There are 2 types of membership operators : 
    1. in
    2. not in
'''



# ************* IN *************

# IN operator returns True if the element on its left is in the sequence at its right
nums = [1,2,3,4,5,6,7,8,9,10]
print("\n\n-------------- List --------------")
print(nums)

print("\n\n-------- IN --------")
print(f"is 1 in nums : {1 in nums}")            # is 1 in nums : True
print(f"is 11 in nums : {11 in nums}")          # is 11 in nums : False



# ************* NOT IN *************

# NOT IN returns True if the element on its left is not in sequence at its right
print("\n-------- NOT IN --------")
print(f"is 11 not in nums : {11 not in nums}")  # is 11 not in nums : True
print(f"is 1 not in nums : {1 not in nums}")    # is 1 not in nums : False