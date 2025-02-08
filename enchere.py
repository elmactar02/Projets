import os

print(r"""
        ______
       |      |
       |  ⚖  |  
       |______|
          ||
          ||
      ==========   
      |        |  
      |  BANG  |  
      |________|  
    """)

print("Bienvenue dans notre enchère: ")
noouv_pers = input("Souhaitez vous enchèrir ? ")

person_mise = {}
while noouv_pers == "oui" :
    os.system('cls' if os.name == 'nt' else 'clear')
    name = str(input("Quel est ton nom ?  "))
    person_mise[name] = int(input("Combien souhaites tu enchèrir ? $"))
    noouv_pers = input("Y'a t'il quelq'un(e) d'autre souhaitant enchèrir ? ")

meilleur_nom = ""
meilleur_mise = 0
for key,value in person_mise.items():
    if value > meilleur_mise:
        meilleur_mise = value
        meilleur_nom = key



print("Et notre grand gagnant est "+meilleur_nom+" avec une mise de $"+str(meilleur_mise))