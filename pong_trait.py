from turtle import Turtle

class trait(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.up()
        self.goto(0,300)
        self.setheading(270)
        self.speed(0)
    
    def draw(self):
        for i in range(0,20)  : 
            self.down()
            self.forward(20)
            self.up()
            self.forward(20)