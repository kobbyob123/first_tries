### A python text game
### This game requires the use of your imagination.
### Functions used : input,if,random

import random
player_name = input("Hello, what's your name? \n")
player_gender = input("\nPlease input your gender : (Male/Female/Other)\n")
player_gender.lower()

if player_gender == 'male':
    print("\nThis is a story about a young hero called " + player_name.title() + ".")
    print(player_name.title() + " is a young boy who loves to play around with his friends.")
    print("His favourite game is 'Rock Paper Scissors'.")

elif player_gender == 'female':
    print("\nThis is a story about a young heroine called " + player_name.title() + ".")
    print(player_name.title() + " is a young girl who loves to play around with her friends.")
    print("Her favourite game is 'Rock Paper Scissors'.")
else:
    print("\nWelcome player.")
    print("\nThis is a story about a young " + player_name.title() + ".")
    print("Your favourite game is 'Rock Paper Scissors'.")

print("\nLet's play it then, shall we?")
answer = input("Do you want to play? (yes/no)\n")
answer.lower()

while answer == "yes":
    print("\nOkay, here we go!!!")
    'Rock Paper Scissors'.center(130,'*')
    
    game1 = ["Rock", "Paper", "Scissors"]
    player_choice = input("\nWhat do you choose?\n")
    random_choice = random.choice(game1)
    print("\nYour opponent had " + random_choice + ".")
    
    if player_choice.title() in game1:
        if player_choice.title() == "Rock" and random_choice == "Paper":
            print("Paper covers rock!")
            print("\nYou lose!!")
            answer = input("\nWill you play again?\n")
        elif player_choice.title() == "Rock" and random_choice == "Scissors":
            print("Rock smashes Scissors!")
            print("\nYou win!!")
            answer = input("\nWill you play again?\n")
        elif player_choice.title() == "Paper" and random_choice == "Rock":
            print("Paper covers rock!")
            print("\nYou win!!")
            answer = input("\nWill you play again?\n")
        elif player_choice.title() == "Paper" and random_choice == "Scissors":
            print("Scissors cuts Paper!")
            print("\nYou lose!!")
            answer = input("\nWill you play again?\n")
        elif player_choice.title() == "Scissors" and random_choice == "Paper":
            print("Scissors cuts Paper!")
            print("\nYou win!!")
            answer = input("\nWill you play again?\n")
        elif player_choice.title() == "Scissors" and random_choice == "Rock":
            print("Rock smashes Scissors!")
            print("\nYou lose!!")
            answer = input("\nWill you play again?\n")
        else:
            print("\nThis is a Draw!!")
            answer = input("\nWill you play again? (yes/no)\n")
    else:
        print("Invalid choice.")
        break

print("\nOkay then, another time!!!")
