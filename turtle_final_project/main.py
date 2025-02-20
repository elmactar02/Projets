import random
import time
from turtle import Screen, Turtle
from player import Player
from car_manager import CarManager
import car_manager as crm
import player as ply
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
joueur_1 = Player()
tableau_de_bord = Scoreboard()
game_over = Turtle(visible=False)
game_over.up()
game_over.setx(-40)
game_over.color("black")
level = 1 

screen.listen()
screen.onkey(joueur_1.move,"Up")
list_voiture = []

game_is_on = True

while game_is_on:
    voiture = CarManager()
    voiture.move()
    list_voiture.append(voiture)
    for voiture in list_voiture[-1::-1]:
        voiture.move()

    for voituree in list_voiture:
        #Comme la taille des voitures n'est pas tout à fait carré si j'utilise distance, et que je met un nombre
        #en fonction de la largeur, si la tortue se trouve en haut dans un espace , le code s'arretera car cette distance en coordonnée y est plus petite du à la taille de sur l'axe y
        if (abs(joueur_1.xcor() - voituree.xcor()) < 30) and (abs(joueur_1.ycor() - voituree.ycor()) < 20.) :
            game_is_on = False
            game_over.write("Game Over",font=("Arial",10,"normal"))
            

    if joueur_1.ycor() > 220 :
        level += 1
        joueur_1.goto(ply.STARTING_POSITION)
        crm.MOVE_INCREMENT += 5
        
    tableau_de_bord.show_level(level)
    time.sleep(0.1)
    
    screen.update()




screen.exitonclick()