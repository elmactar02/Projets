colors = [(245,243,238),(247,242,244),(240, 245, 241), (202, 164, 109), (238, 240, 245), (150, 75, 49), (223, 201, 135),
(18,86, 90), (81, 148, 129), (148, 17, 20), (14, 70, 64), (30, 68, 100), (107, 127, 153), (174, 94, 97), (176, 192, 209)]

from turtle import Turtle, Screen
import turtle
import random
turtle.colormode(255)
def tortue_teleporte(x,y):
    tortue = Turtle(visible=False)
    tortue.teleport(x,y)
    tortue.showturtle()
    return tortue

def draw_a_dot(ma_tortue):
    color = random.choice(colors)
    ma_tortue.color(color)
    ma_tortue.fillcolor(color)
    ma_tortue.down()
    ma_tortue.begin_fill()
    ma_tortue.circle(5)
    ma_tortue.end_fill()
    ma_tortue.up()
ma_tortue = tortue_teleporte(-300,-300)
ma_tortue.shape("arrow")
ma_tortue.speed(0)


for i in range(0,10):
    compteur = 1 
    for j in range(0,20):
        vide = random.randint(0,10)
        nb_aleatoire = random.randint(0,10)
        if nb_aleatoire == vide & compteur != 0 & j!= 19 :
            ma_tortue.forward(25)
        elif j!= 19:
            draw_a_dot(ma_tortue)
            ma_tortue.forward(25)
        elif j==19:
            if nb_aleatoire == vide & compteur != 0 :
                pass
            else:
                draw_a_dot(ma_tortue)
        
    ma_tortue.left(90)
    ma_tortue.forward(25)
    ma_tortue.left(90)
    compteur = 1 
    for j in range(0,20):
        vide = random.randint(0,10)
        nb_aleatoire = random.randint(0,10)
        if nb_aleatoire == vide & compteur != 0 & j!= 19:
            ma_tortue.forward(25)
        elif j!= 19:
            draw_a_dot(ma_tortue)
            ma_tortue.forward(25)
        elif j==19:
            if nb_aleatoire == vide & compteur != 0 :
                print('')
            else:
                draw_a_dot(ma_tortue)
    ma_tortue.right(90)
    ma_tortue.forward(12.5)
    ma_tortue.right(90)




ecran = Screen()
ecran.exitonclick