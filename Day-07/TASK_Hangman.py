import os
import random
from hangman_words import word_list
from hangman_art import logo, stages

# list to hold character
display = []
chosen_word = random.choice(word_list)

# filling list with _ as default values which later gets replaces by correct guesses from user
for _ in chosen_word:
    display += "_"

# 6 lives to guess letters correctly
lives = 6
# while loop conditional iterator
end_of_game = False

print(logo)
print("\n", display)


while not end_of_game:
    user_guess = input("Enter any alphabet as guess : ").lower()
    
    # clearing screen
    os.system("cls")
    
    # if user guessed character which is already guessed
    if user_guess in display:
        print(f"You've already guessed {user_guess}")

    # if user gets correct letters
    for position in range(len(chosen_word)):
        letter = chosen_word[position]
        if letter == user_guess:
            display[position] = letter

    # if user gets wrong letters
    if user_guess not in chosen_word:
        print(f"You guessed {user_guess}, that's not in the word. You lose a life")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print("You lose")
            print(f"The answer was {chosen_word}")

    # converting list to string
    print(f"{' '.join(display)}")

    if "_" not in display:
        end_of_game = True
        print("You win")

    print(stages[lives])