from turtle import Turtle, Screen
import time
from snake import snake
from snake_food import food
from snake_score import score

ecran = Screen()
ecran.setup(width=600,height=600)
ecran.bgcolor("black")

ecran.tracer(0)
snake = snake()
my_food = food()
score_board = score()
with open("high_score.txt","r+") as file:
      highscore= file.read()
score_board.show_score(highscore)

ecran.listen()
ecran.onkey(snake.droite,"Right")
ecran.onkey(snake.gauche,"Left")
ecran.onkey(snake.Haut,"Up")
ecran.onkey(snake.Bas,"Down")

is_true = True
while is_true:
    ecran.update()
    if(abs(snake.snake[0].xcor()) >= 290 or abs(snake.snake[0].ycor()) >= 290):
        with open("high_score.txt","r+") as file:
            if score_board.point > int(file.read()):
                file.seek(0)
                file.write(str(score_board.point))
                highscore = score_board.point
                file.truncate()
        score_board.clear()
        score_board.show_score(highscore)
        is_true = False
    for block in snake.snake[6:]:
        if block.distance(snake.snake[0]) < 20:
            is_true = False
            with open("high_score.txt","r+") as file:
                if score_board.point > int(file.read()):
                    file.seek(0)
                    file.write(str(score_board.point))
                    file.truncate()
                    highscore = score_board.point
            score_board.clear()
            score_board.show_score(highscore)    
    snake.move_snake()
    if my_food.aliment.distance(snake.snake[0]) < 15:
        my_food.move()
        snake.grandir()
        snake.grandir()
        score_board.incrr()
        score_board.clear()
        with open("high_score.txt","r+") as file:
            highscore = file.read()
        score_board.show_score(highscore)


ecran.exitonclick()

