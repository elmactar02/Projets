import time
from turtle import Screen, Turtle
class barre(Turtle):

    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.setheading(90)
        self.shapesize(1,5)
        self.up()
        self.goto(position,0)

    def move_up(self):
        if (self.distance(self.xcor(),300) > 60 ) :
            self.forward(30) 

    def move_down(self):
        if (self.distance(self.xcor(),-300) > 70 ) :
            self.backward(30) 