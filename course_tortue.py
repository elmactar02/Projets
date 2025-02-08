from turtle import Turtle, Screen
import random

Colors = ["blue","red","yellow","green","pink","orange"]


ecran = Screen()
ecran.setup(width=500,height=400)
choix = ecran.textinput("JEU","Selon vous qui gagnera ?")
tortue_list=[] 
taille_list = len(Colors)
for i in range(0,taille_list):
    ma_tortue = Turtle(shape="turtle")
    ma_tortue.color(Colors[i])
    ma_tortue.up()
    ma_tortue.goto(-230,-100 + (30*i))
    tortue_list.append(ma_tortue)

if choix:
    is_race_on= True 
else:
    is_race_on = False

while is_race_on:
    for ma_tortue in tortue_list:
        ma_tortue.forward(random.choice([0,5,2,4]))
        if ma_tortue.xcor() > 230:
            color_gagnant = ma_tortue.pencolor()
            is_race_on = False

if choix == color_gagnant:
    print("Tu avais bien deviné")
else :
    print("Dommage tu as perdu ! "+ color_gagnant + " a gagné")


ecran.exitonclick()