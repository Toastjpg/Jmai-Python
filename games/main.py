import rps
import dice
import hangman


class Game_Menu:
    in_message = """
    >> Welcome to the Arcade!
    >> Please Select from the following options below:
            """
    options = """
            > (0) Exit
            > (1) Rock Paper Scissors
            > (2) Dice Game
            > (3) Hangman
            """
    out_message = """
    >> Thank you for playing! Goodbye...
            """
    cont = True


def start():
    game_start = Game_Menu()

    while game_start.cont:
        print(game_start.in_message)
        print(game_start.options)
        user_in = int(input("> "))
        if user_in == 0:
            print(game_start.out_message)
            game_start.cont = False
        elif user_in == 1:
            rps.start()
        elif user_in == 2:
            pass
        elif user_in == 3:
            pass


if __name__ == '__main__':
    start()
