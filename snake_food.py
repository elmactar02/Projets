from turtle import Turtle
import random
class food:

    def __init__(self):
        self.aliment = Turtle()
        self.aliment.shape("circle")
        self.aliment.shapesize(0.5)
        self.aliment.color("blue")
        self.aliment.speed(0)
        self.aliment.up()
        self.aliment.goto(random.choice(range(-280,280)),random.choice(range(-280,280)))

    def move(self):
        self.aliment.goto(random.choice(range(-280,280)),random.choice(range(-280,280)))