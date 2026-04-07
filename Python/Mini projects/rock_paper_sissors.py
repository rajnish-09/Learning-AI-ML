# Python program to play rock paper sissors game
import random

choices = ["Rock", "Paper", "Scissors"]

user_choice = int(input("Enter 0 for Rock, 1 for Paper, 2 for Scissors: "))

if user_choice not in [0, 1, 2]:
    print("Invalid input")
else:
    computer_choice = random.randint(0, 2)
    print("You:", choices[user_choice])
    print("Computer:", choices[computer_choice])

    if user_choice == computer_choice:
        print("Draw")
    # \ is a line continuation character
    elif (user_choice == 0 and computer_choice == 2) or \
         (user_choice == 1 and computer_choice == 0) or \
         (user_choice == 2 and computer_choice == 1):
        print("You won")
    else:
        print("Computer won")