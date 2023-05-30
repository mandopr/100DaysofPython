print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print('''\n\n--------------------------------------------------
        Welcome to Treasure Island!
--------------------------------------------------''')


print("\nYour mission is to find the treasure.")

direction = input('\nYou\'re at cross road. Where do you want to go? Type "left" or "right" : ').lower()

if direction == "left":
    swim_or_wait = input('You\'ve come to lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across : ').lower()
    if swim_or_wait == "wait":
        door = input('You arrived at the island unharmed. There is a house with 3 door. One red, one yellow and one blue. Which color do you choose? : ').lower()
        if door == "yellow":
            print("\nYou found the treasure! You win!")
        elif door == "red":
            print("\nIt's a room full of fire. Game Over.")
        elif door == "blue":
            print("\nYou enter a room of beast. Game Over.")
        else:
            print("\nYou chose a door that doesn't exist. Game Over.")

    elif swim_or_wait == "swim":
        print("\nYou got attacked by an angry trout. Game Over.")
    else:
        print("\nChoose valid choice!")
elif direction == "right":
    print("\nYou fell into a hole. Game Over.")
else:
    print("\nChoose valid choice!")