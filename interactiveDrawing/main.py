import turtle

test = turtle.Turtle()

loop = True

while loop:
    userIn = input(">>> ")

    if userIn == "n":
        loop = False
    elif userIn == "f":
        test.forward(50)
    elif userIn == "s":
        test.stamp()
    elif userIn == "r":
        test.right(90)
    elif userIn == "l":
        test.left(90)