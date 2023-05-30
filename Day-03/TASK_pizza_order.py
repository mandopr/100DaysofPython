print('''\n\n--------------------------------------------------
        Welcome to Python Pizza Deliveries!
--------------------------------------------------''')
size = input("\nWhat size of pizza do you want? S, M or L : ")
add_pepperoni = input("Do you want pepperoni? Y or N : ")
add_chesse = input("Do you wanr extra cheese? Y or N : ")

bill = 0
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Enter valid size !!")

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

if add_chesse == "Y":
    bill += 1

print(f"Your final bill will be ${bill} for {size} size pizza")