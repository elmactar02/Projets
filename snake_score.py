from turtle import Turtle
class score(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.color("white")
        self.up()
        self.goto(0,270)
        self.point = 0 
        
    def show_score(self,highscore):
        self.write(f"Votre score est de {self.point} , High score: {highscore}",align="center")
    def incrr(self):
        self.point +=1