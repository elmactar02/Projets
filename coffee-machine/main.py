from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
import time, os
print("Démarrage de la machine à café ...")
time.sleep(5)
os.system('cls')
choix = ""
menu = Menu()
machine_a_cafe = CoffeeMaker()
tirelire = MoneyMachine()

while choix != "off":
    choix = input("Que souhaitez vous boire ? "+ menu.get_items()+" :")
    if choix == "off":
        break
    cafe_choisi = menu.find_drink(choix)
    if choix == "report":
        machine_a_cafe.report()
        tirelire.report()
    elif machine_a_cafe.is_resource_sufficient(cafe_choisi) and tirelire.make_payment(cafe_choisi.cost):
        machine_a_cafe.make_coffee(cafe_choisi)
    else:
        break