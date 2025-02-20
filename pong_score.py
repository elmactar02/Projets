from turtle import Turtle


class score(Turtle):

    def __init__(self):
        super().__init__(visible=False)
        self.color("white")
        self.score1 = 0
        self.score2 = 0
        self.up()
        self.goto(-35,230)
    def show_score(self):
        self.clear()
        self.write(f"{self.score1} {self.score2}",font=("Arial",40,"normal"))
        
