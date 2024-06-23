import turtle
import random

tim = turtle.Turtle()
turtle.colormode(255)

colours = ["CornflowerBlue", "DarkOrchid", "IndianRed", "DeepSkyBlue", "LightSeaGreen", "wheat", "SlateGray",
           "SeaGreen"]


# directions = [0, 90, 180, 270]


def rand_col():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_colours = (r, g, b)
    return random_colours


tim.speed("fastest")


def draw_circle(size):
    for _ in range(int(360 / size)):
        tim.color(rand_col())
        tim.circle(100)
        tim.setheading(tim.heading() + size)


draw_circle(5)
