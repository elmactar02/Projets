STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
import time
from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.setheading(90)
        self.color("grey")
        self.up()
        self.goto(STARTING_POSITION)

    def move(self):
        if self.ycor != FINISH_LINE_Y:
            self.forward(MOVE_DISTANCE)
    
