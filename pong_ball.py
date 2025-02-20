from turtle import Turtle
import time
class balle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(1)
        self.up()
        self.color("white")
        self.vx = 6
        self.vy = 6

    def move(self):
        self.goto(self.xcor() +self.vx , self.ycor() + self.vy)
        if self.ycor() > 290 or self.ycor() < -290:
            self.vy = -self.vy 
        time.sleep(0.05)