MENU = {
    "espresso":{
        "ingredients":{
            "water": 50,
            "coffee": 10
        },
        "cost": 1.5
    },
    "latte":{
        "ingredients":{
            "water": 200,
            "milk": 150,
            "coffee": 24
        },
        "cost": 2.5
    },
    "cappuccino":{
        "ingredients":{
            "water": 250,
            "milk": 100 ,
            "coffee": 24
        },
        "cost": 1.5
    }
}

Ressources = {
    "water": 300,
    "milk": 300,
    "coffee": 76 ,
    "money": 0
}
import time, os
print("Démarrage de la machine à café ...")
time.sleep(5)
os.system('cls')
choix = ""
def verif_ressources(choix):
    if (Ressources["water"] >= MENU[choix]["ingredients"]["water"]) & (Ressources["milk"] >= MENU[choix]["ingredients"]["milk"]) & (Ressources["coffee"] >= MENU[choix]["ingredients"]["coffee"]):
        return True
    elif (Ressources["water"] < MENU[choix]["ingredients"]["water"]):
        print("Pas assez d'eau !")
        return False
    elif (Ressources["milk"] < MENU[choix]["ingredients"]["milk"]):
        print("Pas assez de lait !")
        return False
    elif (Ressources["coffee"] < MENU[choix]["ingredients"]["coffee"]):
        print("Pas assez de café !")
        return False
   
def deduction_ressources(choix):
    Ressources["water"] -= MENU[choix]["ingredients"]["water"]
    Ressources["milk"] -= MENU[choix]["ingredients"]["milk"]
    Ressources["coffee"] -= MENU[choix]["ingredients"]["coffee"]
    Ressources["money"] += MENU[choix]["cost"]
 
while choix != "off" :
    choix = input("Que souhaitez vous ? (espresso,latte,cappuccino): ")
    if choix == "off":
        break
    if choix == "report":
        print("Water: "+ str(Ressources["water"])+ " ml")
        print("Milk: "+ str(Ressources["milk"])+ " ml")
        print("Coffee: "+ str(Ressources["coffee"])+ " g")
        print("Money: $"+ str(Ressources["money"]))
    else:
        resrc_choix = verif_ressources(choix)
        if not resrc_choix :
            break
        print("Inserer des pièces !")
        centime25 = int(input("Nombre de Pieces de 25 centimes : "))
        centime10 = int(input("Nombre de Pieces de 10 centimes : "))
        centime5 = int(input("Nombre de Pieces de 5 centimes : "))
        centime = int(input("Nombre de Pieces de 1 centime : "))
        total = (centime25 * 0.25 ) + (centime10 * 0.10 ) + (centime5 * 0.05 ) + (centime * 0.01 )
        monnaie = round(total - MENU[choix]["cost"],2)
        if monnaie < 0:
            print("Crédit insuffisant ! ")
            break
        elif monnaie > 0:
            print("Voici vôtre monnaie : $"+str(monnaie))
        print("Préparation de vôtre café ...")
        time.sleep(3)
        deduction_ressources(choix)
        print("Voila ☕ ! Savourez votre café :) ")
        time.sleep(3)
        os.system('cls')