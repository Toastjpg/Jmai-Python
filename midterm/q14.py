import turtle

screen = turtle.Screen()
bot = turtle.Turtle()


def draw_square(size, count):
    for i in range(count):
        for j in range(4):
            bot.forward((i * size) + size)
            bot.left(90)


draw_square(20, 5)
screen.exitonclick()
