from turtle import Turtle, Screen


ma_tortue = Turtle()
ma_tortue.shape("arrow")

def avancer():
    ma_tortue.forward(15)

def reculer():
    ma_tortue.backward(15)

def tourner_droite():
    ma_tortue.right(20)

def tourner_gauche():
    ma_tortue.left(20)


ecran = Screen()
ecran.listen()
ecran.onkey(avancer,"Up")
ecran.onkey(tourner_droite,"Right")
ecran.onkey(tourner_gauche,"Left")
ecran.onkey(reculer,"Down")

ecran.exitonclick()