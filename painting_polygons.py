from turtle import Turtle , Screen
import random
# Trait coupé : tortue = Turtle(visible=False)
#tortue.shape("arrow")

#tortue.teleport(-300,-300)

#tortue.showturtle()
#for i in range(0,50):
#    tortue.forward(5)
#    tortue.up()
#    tortue.forward(5)
#    tortue.down()
def tortue_teleporte(x,y):
    tortue = Turtle(visible=False)
    tortue.teleport(x,y)
    tortue.showturtle()
    return tortue

def dessiner(tortue,nb_cotes):
    angle = 360 / nb_cotes
    colors = ["red","green","blue","bisque3","DarkGoldenrod","coral4","gray","gold","firebrick","indianRed","khaki2"]
    color = random.choice(colors)
    tortue.color(color)
    tortue.fillcolor(color)
    for i in range(0,nb_cotes):
        tortue.forward(100)
        tortue.right(angle)
    
    
tortue = tortue_teleporte(0,300)
tortue.shape("arrow")
nb_dessin = 10 
nb_cotes = 4
while nb_dessin != 0 :
    dessiner(tortue,nb_cotes) 
    nb_dessin -= 1
    nb_cotes += 1

ecran = Screen()
ecran.exitonclick()