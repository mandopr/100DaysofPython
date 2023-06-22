# ****************************
#          DICTIONARY
# ****************************

'''
    -> Dictionary is python data structure which stores data in key-value form
    -> Key are mostly immutable types like strings, tuple, integers etc ... while values on other can be both mutable and immutable

    
    Syntax :
    --------- 
    dictionary_name = {
        key : value,
        ...
    }

    Here key and value are seperated by colons (:) and each key-value pair is seperated by coma (,).
'''

fav_chars = {
    "Naruto" : 106,             # :P
    "AOT" : ["Levi", "Erwin"],
    "DS" : "Rengoku",
    "JJK" : "Gojo",
    "OPM" : "Saitama"
}


print(f"\nFavourite characters : {fav_chars}")

# we can access dictionary's value by its key in almost similiar way as of list's
print(f"\nFavourite char from Naruto : {fav_chars['Naruto']}")
# NOTE : if on not finding the key specified in code, python will throw KeyError


# we can also update value's of particular key like below : 
fav_chars["OPM"] = "Garou"
print(f"\nFavourite char from OPM after update : {fav_chars['OPM']}")

# If key is not found in above(updation) process, then it will make new key of its own
fav_chars["Vagabond"] = ["Mushashi", "Kojiro"]
print(f"\nUpdated favchar dictionary : {fav_chars}")

# deleting/removing items from dictionary with the help of "del" keyword
del fav_chars["DS"] 
print(f"\nAfter deleting item from favchar dictionary : {fav_chars}")


# clearing dictionary
# fav_chars = {}
print(f"\nEmpty favchar dictionary : {fav_chars}")





# ######################
#   DICTIONARY METHODS
# ######################


print("\n\n\n\n*************** Dictionary methods ***************")



# *************** get() ***************

# get() will retrive value for the specified key
# takes only one parameter which is the key of which we have to find value of
# return the value for the specified key
print(f"\nFavourite character from JJK : {fav_chars.get('JJK')}")
# NOTE : if the key didn't found, it will return None



# *************** items() ***************

# items() will give key/value in form of tuples
# takes zero paramters
# returns a view object that display a list of key/value pair in tuples
print(f"\nView object of list of key/value pair in tuple : {fav_chars.items()}")



# *************** keys() ***************

# keys() will give list of keys in view object
# takes zero paramters
# returns list of keys in view object
print(f"\nAnime names (Keys) : {fav_chars.keys()}")



# *************** values() ***************

# values() will give list of values in view object
# takes zero paramters
# returns list of values in view object
print(f"\nFav chars from anime (Values) : {fav_chars.values()}")



# *************** pop() ***************

# pop() will remove the item of an specified key from the dictionary
# takes two parameters :
#   i) key as parameter to remove that item
#  ii) default as parameter for the value to return if key of first parameter odesn't found
# returns item if key is there, else default value if specified in parameters or else KeyError
fav_chars.pop("OPM")
print(f"\nAfter popping, favchar dictionary : {fav_chars}")



# *************** len() ***************

# len() will give no. of items in dictionary
# takes zero parameters
# return no. of items in dictionary
print(f"\nLength of dictionary : {len(fav_chars)}\n")



# *************** looping over dictionary ***************

for key in fav_chars:
    print(f"{key} : {fav_chars[key]}")
# NOTE : we can loop through dictionary but instead of returning a item it will return keys of it

print("\n")
for key, value in fav_chars.items():                       # other way of iterating over dictionary's item by getting key and value directly with items()
    print(f"{key} : {value}")
