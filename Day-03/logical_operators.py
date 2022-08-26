# ****************************
#      LOGICAL OPERATORS
# ****************************

# logical operators as name says perform logical operations (-_-)
# another use-case of logical operator is when there is two much of if-elif we can replace them with logical operators

'''
    Types of logical operators : 

    'and' / &&        ->      logical 'and' operator (will evalute True only if condition on both side of 'AND' evalutes to True)
    'OR' / ||         ->      logical 'OR' operator (will evaluate True even if one condition of either side of 'OR' evaluates to True)
    'NOT'             ->      logical 'NOT' operator (will reverse the answer, if the answer is True NOT will make it False and vise-versa)
'''

print((10 > 5) and (10 > 9))
print((10 > 5) or (10 > 19))
print(not (10 > 5))
