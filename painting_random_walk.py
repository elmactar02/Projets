from turtle import Turtle, Screen
import turtle as t
import random

t.colormode(255)
def tortue_teleporte(x,y):
    tortue = Turtle(visible=False)
    tortue.teleport(x,y)
    tortue.showturtle()
    return tortue

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

def random_walk(tortue):
    nb= random.randint(0,4)
    tortue.color(random_color())
    direction = random.randint(25,135)
    if nb == 0:
        tortue.right(direction)
        tortue.forward(40)
    elif nb == 1 :
        tortue.left(direction)
        tortue.forward(40)
    elif nb == 3:
        tortue.forward(40)
    else :
        tortue.backward(40)


ma_tortue = tortue_teleporte(-100,0)
ma_tortue.width(10)
ma_tortue.speed(7)
for i in range(0,200):
    random_walk(ma_tortue)



ecran = Screen()
ecran.exitonclick