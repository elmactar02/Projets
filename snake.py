from turtle import Turtle
import time
class snake:

    def __init__(self):
        self.snake = []
        for i in range(0,3):
            new_block = Turtle()
            new_block.color("white")
            new_block.shape("square")
            new_block.up()
            if i == 1 :
                new_block.setx(-20)
            elif i == 2:
                new_block.setx(-40)

            self.snake.append(new_block)
    def move_snake(self):
        i = len(self.snake) - 1
        for i in range(i,0,-1):
            self.snake[i].goto(self.snake[i-1].xcor(),self.snake[i-1].ycor())
        self.snake[0].forward(10)
        time.sleep(0.04)
    def droite(self):
        if self.snake[0].heading() == 90:
            self.snake[0].setheading(0)
        elif self.snake[0].heading() == 270:
            self.snake[0].setheading(0)
    def gauche(self):
        if self.snake[0].heading() == 90:
            self.snake[0].setheading(180)
        elif self.snake[0].heading() == 270:
            self.snake[0].setheading(180)

    def Haut(self):
        if self.snake[0].heading() == 180:
            self.snake[0].setheading(90)
        elif self.snake[0].heading() == 0:
            self.snake[0].setheading(90)
    def Bas(self):
        if self.snake[0].heading() == 0:
            self.snake[0].setheading(270)
        elif self.snake[0].heading() == 180:
            self.snake[0].setheading(270)

    def grandir(self):
        new_block = Turtle()
        new_block.color("white")
        new_block.shape("square")
        new_block.up()
        if self.snake[0].heading() == 0:
            new_block.setx(self.snake[-1].xcor() - 20 )
            new_block.sety(self.snake[-1].ycor())
            self.snake.append(new_block)
        elif self.snake[0].heading() == 90:
            new_block.setx(self.snake[-1].xcor() )
            new_block.sety(self.snake[-1].ycor() - 20)
            self.snake.append(new_block)
        elif self.snake[0].heading() == 180 :
            new_block.setx(self.snake[-1].xcor() + 20 )
            new_block.sety(self.snake[-1].ycor())
            self.snake.append(new_block)
        elif self.snake[0].heading() == 270:
            new_block.setx(self.snake[-1].xcor())
            new_block.sety(self.snake[-1].ycor() + 20)
            self.snake.append(new_block)