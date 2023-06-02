# ****************************
#            LIST
# ****************************

'''
    -> list can be described as the data structure which holds data in ordered manner.
    -> list are indicated by [] brackets.
    -> We can say it is array of python but unlike other programming languages its not bounded by limited indexes,
       python has built-in performance which automatically creates more indexes when needed.
    -> List holds similiar data (data related to one entity), but it can have multiple types of data in it.
    -> List can hold integer, string, another lists etc ...
'''

# list is created with square brackets [], and we can write data in it by seperating them with commas (,).
fav_chars = ['Itachi', 'Shisui', 'Minato', 'Obito']
print(f"\n\tList : {fav_chars} \n")





# *************** INDEX OPERATOR ***************

# Just like string as iterable we can also take out specific element from list by index operator
# index operator can be used in program with square brackets and index in it.
# index in python starts from 0, so first element will be on 0th index, second element will be on 1st index and so on...
# indexing can be done with negative index as well

print(f"\tFirst fav char : {fav_chars[0]}")
print(f"\tLast fav char : {fav_chars[-1]}")





# *************** SLICE OPERATOR ***************

'''
    -> with the help of slice operator we can extract range of elements from list.
    -> slice operator is denoted by [:].

    SYNTAX -> listname[<starting index> : <ending index>]

    -> Here <starting index> represents from where would we start extracting elements from list.
    -> Here <ending index> represents upto where would we extracting elements from list.
    -> <ending index> is exlusive of range, which means it will extract upto that index not including it.
    -> we can also apply negative indexing to starting and ending index in slicing.

    -> remember indexing starts from 0th index in python.
    -> if we skip the <starting index>, slice operator will start slicing from 0th index
       and if we skip the <ending index> it will slice upto the (n-1)th index (last index) of the list
'''

top_three_fav_char = fav_chars[0:3]
print(f"\tTop three favchars : {top_three_fav_char}")





# *************** MODIFING LIST ELEMENT ***************

# with the help of indexing and assignment operator we can access a particular position and change value on it.
fav_chars[-1] = 'Madara'
print(f"\n\tAfter modifing element of fav_chars : {fav_chars}")

# we can even modify range of elements with slice operator
fav_chars[1:3] = ['Naruto', 'Orochimaru']
print(f"\tAfter modifing range of elements from fav_chars : {fav_chars}")





# *************** DELETING LIST ELEMENT ***************

# with the help of indexing and del operator we can delete a particular element
del fav_chars[-1]
print(f"\n\tAfter deleting last element : {fav_chars}")

# we can also delete range of elements from list with the help of slice operator.
del fav_chars[2:]
print(f"\tAfter deleting range of elements : {fav_chars}")





# ################
#   LIST METHODS
# ################



# *************** append() ***************

# append() will add new element at the end of the list.
# it take only one parameter which is the item we want to append.
# it doesn't return any thing.
fav_chars.append('Minato')
print(f"\n\tAfter append : {fav_chars}")



# *************** insert() ***************

# insert() will add new element at the specified index in the list.
# it takes two parameters, first the index at which we want ot add element and second is the element we want to add.
# it doesn't return anything.
fav_chars.insert(1, "Madara")
print(f"\tAfter insert : {fav_chars}")



# *************** remove() ***************

# remove() will remove the first occurence of passed element from the list.
# it takes only parameter which we want to remove from the list.
# it doesn't return anything.
# if the passed element doesn't found, it will throw exception.
fav_chars.remove('Naruto')
print(f"\n\tAfter remove : {fav_chars}")



# *************** pop() ***************

# pop() will remove the element at the specified index from the list.
# it takes single parameter which the index at which we want to remove element.
# it return poped element.
print(f"\tPoped element : {fav_chars.pop(1)}")



# *************** extend() ***************

# extend() will add elements/items of the list/tuple/set into list.
# it takes only one parameter which is the iterator we want to extend with.
# it doesn't return anything.
other_favchars = ['Jiraya', 'Shikamaru']
fav_chars.extend(other_favchars)
print(f"\n\tAfter extend : {fav_chars}")

# NOTE : extends() will add elements of iterator at the end while append() will add whole iterator at last.



# *************** index() ***************

# index() will return the index of specified element within the list.
# it will return index of only first occurence of specified element.
# it takes only one parameter which is the element of which we want index of.
# it returns the index of first occurence of specified element.
# on not finding specified element in list, it will throw exception.
print(f"\n\tIndex of Minato : {fav_chars.index('Minato')}")



# *************** count() ***************

# count() will return the number of times specified element occurse in the element.
# it will take only one argument which is the element we want to find count occurence of.
# it returns the number of time specified element occurs.
print(f"\n\tCount of Itachi : {fav_chars.count('Itachi')}")



# *************** reverse() ***************

# reverse() will reverse the list.
# it doesn't have any parameter.
# it doesn't return anything.
# will make changes in actuall list.
fav_chars.reverse()
print(f'\n\tReversed list : {fav_chars}')



# *************** sort() ***************

# sort() will sort elements of list ascendingly or descendingly.
# it has two parameters which are optional but can be useful.
# it doesn't return anything.
# key parameter is used to create function with which we can sort list by other ways
fav_chars.sort()
print(f"\n\tList in ascending order : {fav_chars}")

fav_chars.sort(reverse=True)
print(f"\n\tList in descending order : {fav_chars}")



# *************** copy() ***************

# copy() will return a shallow copy of the list.
# it doesn't have any paramteres.
# it returns new list which is shallow copy of list.

copy_favchar = fav_chars.copy()
print(f"\n\tShallow copy : {copy_favchar}")



# *************** len() ***************

# len() will return the length of the list
# it takes one parameter which is the iterator of which we want length of
# it returns the length of iterator.
print(f"\n\tLength of favchar list : {len(fav_chars)}")



# *************** clear() ***************

# clear() will clear the list/remove all the elements of list.
# it doesn't take any parameter nor return any thing.
fav_chars.clear()
print(f"\n\tEmpty favchar : {fav_chars}")