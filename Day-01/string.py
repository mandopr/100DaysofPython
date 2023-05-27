# **************************
#           STRING
# **************************

# A string is sequence of characters enclosed within single/double (' / ") quotes.
print('This is string enclosed in single quotes')           # This is string enclosed in single quotes
print("This is string enclosed in double quotes")           # This is string enclosed in double quotes



# ************* Escape Sequence *************

# what if we need same quotes in string which is surrounding it, escape sequence will be used in this situations
# we will use ( \ ) backslash before quotes to use them in actual string
print("Hello \"World\"")            # Hello "World"

# we can use : 
    # \n for new line
    # \t for tab
    # \' for using single qutoe
    # \" for using double quote
    # and much more



# ************* String Concatenation *************

# In simple words string concatenation means adding/joining/attaching two or more strings together
# with the help of + operator we can concatenate strings with each other
print("String" + " " + "Concatenation")         # String Concatenation
# NOTE : notice that we use an string with space to create space between two words, we can also give it in on of the words as well.




# ************* String Indexing / Substring *************

# we can access any string's character via help of indexing.
# string is python iterable object (which we will focus on later), which means we can iterate over on.
# indexing in python starts with 0 (not 1), so first element/character of iterable object is on 0th index and so on...
# indexing is done with the help of square brackets ( [] ), and by writing index number within them.
print("Hello"[0])           # H

# we can index character from negative indexing which starts from -1, last second element is on -2nd index and so on...
print("Hello"[-1])          # o




# ************* F strings *************

# concatenating string is shit tone of work to do, f-strings is your hero now
'''
    all we need to do is simply put (f) before quotes in string and whenever you want to perform some operations
    add curly braces {}, within quotes like below
'''
name = "Itachi Uchiha"
print(f"Hey {name}")            # Hey Itachi Uchiha