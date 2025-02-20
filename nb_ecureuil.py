import pandas as pd

#Trouver le nombre d'ecureils par couleurs
data_brute = pd.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20250215.csv")

new_data = data_brute[data_brute["Primary Fur Color"].isna() == False].groupby("Primary Fur Color").size()

print(new_data)