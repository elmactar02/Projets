COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 9
import random
from turtle import Turtle


class CarManager(Turtle):
    
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.up()
        self.speed(0)
        self.shape("square")
        self.shapesize(1,2)
        self.setheading(180)
        self.setx(280)
        list = range(-220,220)
        list_2 = list[::50]
        self.sety(random.choice(list_2))
        self.forward(STARTING_MOVE_DISTANCE)

    def move(self):
        self.forward(MOVE_INCREMENT)

