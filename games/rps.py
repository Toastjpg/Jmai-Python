import random

in_message = ">> Welcome to RPS!"
options = """>> Choose one of the following options:
        > (0) Exit
        > (1) Rock
        > (2) Paper
        > (3) Scissors
"""
out_message = """
    >> Thank you for playing! Goodbye...
"""
tie = ""
win = ""
loss = ""


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


def start():
    cont = True
    print(in_message)

    while cont:
        comp_in = random.randint(1, 3)
        print(options)
        user_in = int(input("> "))
        if user_in == 0:
            print(out_message)
            cont = False
        elif user_in == 1:
            print(compare(user_in, comp_in))
        elif user_in == 2:
            print(compare(user_in, comp_in))
        elif user_in == 3:
            print(compare(user_in, comp_in))
        else:
            return "Invalid Input..."
