import turtle as t
import random

tim = t.Turtle()    # assigns tim to class in turtle module
t.colormode(255)    # access turtle module directly and changes the color mode

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color = (r, g, b)    #Create a tuple
    return random_color

direction = [0, 90, 180, 270]
tim.pensize(15)
tim.speed("fastest")

for _ in range (200):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(random.choice(direction))

