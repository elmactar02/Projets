from turtle import Turtle, Screen
import turtle as trt
import pandas as pd
ecran = Screen()
ecran.title("US State finder")

image = "blank_states_img.gif"
ecran.addshape(image)
trt.shape(image)

game_is_on = True
df_localisations = pd.read_csv("50_states.csv")

while game_is_on:
    etat = ecran.textinput("Guess the state",prompt="Write a state name")
    line = df_localisations[df_localisations["state"] == etat]
    print(line)
    if not line.empty:
        text = Turtle(visible=False)
        text.up()
        text.goto(float(line["x"].iloc[0])-20,float(line["y"].iloc[0]))
        text.down()

        text.write(etat)
    else:
        game_is_on = False




ecran.exitonclick()