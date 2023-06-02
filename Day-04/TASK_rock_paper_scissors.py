import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for rock, 1 for paper and 2 for scissors : "))

if user_choice >= 3 and user_choice < 0:
    print("\nInvalid choice, you lose")
else:
    computer_choice = random.randint(0,2)

    print(f"\nYou choose : \n{game_images[user_choice]}")
    print(f"\nComputer choose : \n{game_images[computer_choice]}")

    if user_choice == 0 and computer_choice == 2:
        print("\nYou win")
    elif user_choice == 2 and computer_choice == 0:
        print("\nYou lose")
    elif user_choice > computer_choice:
        print("\nYou win")
    elif user_choice == computer_choice:
        print("\nIt's draw")
    else:
        print("\nYou lose")
