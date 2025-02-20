import random
from turtle import Turtle , Screen
from pong_barre import barre
from pong_ball import balle
from pong_score import score
from pong_trait import trait
ecran = Screen()
ecran.bgcolor("black")
ecran.setup(600,600)

ecran.tracer(0)
barre_1 = barre(270)
barre_2 = barre(-270)
balle_1 = balle()
score_count = score()
trait_vert = trait()
trait_vert.draw()

ecran.listen()
ecran.onkeypress(barre_1.move_up,"Up")
ecran.onkeypress(barre_1.move_down,"Down")
ecran.onkeypress(barre_2.move_up,"a")
ecran.onkeypress(barre_2.move_down,"w")

game_on = True
while game_on:
    ecran.update()
    balle_1.move()
    score_count.show_score()
    if (balle_1.distance(300,balle_1.ycor()) < 6 ) :
        score_count.score1 +=1
        balle_1.goto(0,0)
        balle_1.vx = random.choice([-6,6,7])
        balle_1.vy = random.choice([-6,6,7])
        if score_count.score1 == 5 :
            score_count.show_score()
            game_on = False
    elif (balle_1.distance(-300,balle_1.ycor()) < 6 ):
        score_count.score2 +=1
        balle_1.goto(0,0)
        balle_1.vx = random.choice([-6,6,7])
        balle_1.vy = random.choice([-6,6,7])
        if score_count.score2 == 5 :
            score_count.show_score()
            game_on = False
    if balle_1.distance(barre_1) < 25 or balle_1.distance(barre_2) < 25 :
        balle_1.vx = - balle_1.vx
        balle_1.goto(balle_1.xcor() + balle_1.vx, balle_1.ycor()) 


ecran.exitonclick()