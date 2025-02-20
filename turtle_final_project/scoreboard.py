FONT = ("Courier", 24, "normal")
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__(visible=False)
        self.up()
        self.goto(-250,250)
    
    def show_level(self,level):
        self.clear()
        self.write(f"Level {level}",font=FONT)
