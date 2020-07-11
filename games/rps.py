import random


class RPS:
    in_message = "     >> Welcome to RPS!"
    options = """     >> Choose one of the following options:
            > (0) Exit
            > (1) Rock
            > (2) Paper
            > (3) Scissors
    """
    out_message = """
        >> Thank you for playing! Goodbye...
    """
    cont = True

# Generates a random computer choice
    @staticmethod
    def comp_choice():
        return random.randint(1, 3)

# Compares user input and generated comp input
    @staticmethod
    def compare(user_in, comp_in):
        if user_in == comp_in:
            return "Tie!"
        elif (user_in == 1) and (comp_in == 2):
            return "Loss! Rock loses against Paper..."
        elif (user_in == 1) and (comp_in == 3):
            return "Win! Rock wins against Scissors..."
        elif (user_in == 2) and (comp_in == 1):
            return "Win! Paper wins against Rock..."
        elif (user_in == 2) and (comp_in == 3):
            return "Loss! Paper loses against Scissors..."
        elif (user_in == 3) and (comp_in == 1):
            return "Loss! Scissors loses against Rock..."
        elif (user_in == 3) and (comp_in == 2):
            return "Win! Scissors win against Paper..."
        return "Invalid Input"

# Create a scoring system, possibly global points?


def start():
    game = RPS()
    print(game.in_message)

    while game.cont:
        print(game.options)
        user_in = int(input("> "))
        if user_in == 0:
            print(game.out_message)
            game.cont = False
        elif user_in == 1:
            comp_in = game.comp_choice()
            print(game.compare(user_in, comp_in))
        elif user_in == 2:
            comp_in = game.comp_choice()
            print(game.compare(user_in, comp_in))
        elif user_in == 3:
            comp_in = game.comp_choice()
            print(game.compare(user_in, comp_in))
