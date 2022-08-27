# ****************************
#            LIST
# ****************************

'''
    -> list can be described as the data structure which holds data in ordered manner.

    -> We can say it is array of python but unlike other programming languages its not bounded by limited indexes,
       python has built-in performance which automatically created more indexes when needed.
    -> List holds similiar data (data related to one entity), but it can have multiple types of data in it.
    -> List can hold integer, string, another lists etc ...
'''

# list is created with square brackets [], and we can write data in it by seperating them with commas (,).
fav_chars = ['Itachi', 'Shisui', 'Minato', 'Madara']
print(fav_chars)





# *************** INDEX OPERATOR ***************

# Just like string as iterable we can also take out specific element from list by index operator
# index operator can be used in program with square brackets and index in it.
# index in python starts from 0, so first element will be on 0th index, second element will be on 1st index and so on...

print(f"First fav char : {fav_chars[0]}")
