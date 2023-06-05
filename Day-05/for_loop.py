# ****************************
#           FOR LOOP
# ****************************

# for loop is used to iterate over sequences or range of numbers

'''
    SYNTAX : 
    
    for <loop_counter> in <sequence> : 
        code block of for loop ...


    -> 'for' is keyword used to start for
    -> <loop_counter> which holds the counter/element from the sequence of for loop
    -> 'in' which is membership operator and
    -> <sequence> on which we have to iterate over with for loop and this 
    -> here : represents that from below we have code block of for loop indented
'''


favchars = ["Itachi", "Shisui", "Minato", "Madara"]
for favchar in favchars:
    print(favchar)