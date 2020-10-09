#######################
#
# Johnny Mai
# 2020-09-24
# Chatbot with a loop! (and a game)
#
########################

import random

print("Hello! Would you like to play a game?")
reply = input(">>> ").lower().strip(" !@#$%^&*()_+{}[]:;'\"<>,.?/|\\")

if reply in ["yes", "y", "yea", "yeah", "ok", "sure"]:
    print("Ok, best of 3!")
    possibleChoice = ["r", "p", "s"]

    # Plays rock paper scissors loop 3 times
    for count in range(3):
        print("\n(R)ock, (P)aper, or (S)cissors?")
        # Grabs user input (r, p , or s) and strips unnecessary characters
        userChoice = input(">>> ").lower().strip("!@#$%^&*()_+{}[]:;'\"<>,.?/|\\")
        compChoice = random.choice(possibleChoice)

        # Compares user and comp choice
        if userChoice == compChoice:
            print(f"Tie! we both choice {userChoice}")
        elif (userChoice == "r") and (compChoice == "p"):
            print(f"You lost! I chose {compChoice}")
        elif (userChoice == "r") and (compChoice == "s"):
            print(f"You win! {userChoice} beats {compChoice}")
        elif (userChoice == "p") and (compChoice == "r"):
            print(f"You win! {userChoice} beats {compChoice}")
        elif (userChoice == "p") and (compChoice == "s"):
            print(f"You lost! I chose {compChoice}")
        elif (userChoice == "s") and (compChoice == "r"):
            print(f"You lost! I chose {compChoice}")
        elif (userChoice == "s") and (compChoice == "p"):
            print(f"You win! {userChoice} beats {compChoice}")
        else:
            print("Invalid input.")

    print("\nGood game! Lets play again another time.")

elif reply in ["no", "n", "nah", "no thanks", "nope"]:
    print("Oh that's too bad. See you next time then...")

else:
    print("Im sorry, I dont understand...")
