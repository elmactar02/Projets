import random
nombre = random.randint(0,100)
def is_equal(choix):
    if(choix < nombre):
        print("C'est plus !")
    elif choix > nombre:
        print("C'est moins !")
    else:
        print("Vous avez trouvé, le nombre était "+str(nombre))
print("Bienvenue dans le jeu de devine-nombre !")
niveau = input("Quel niveau souhaites tu ? (facile , difficile) : ")
essais = 0
if( niveau == "facile"):
    essais = 10
else:
    essais = 5

print("Vous avez "+str(essais)+" essais")
choix = int(input("Nombre choisi entre 0 et 100 ! Votre choix : "))
is_equal(choix)
essais -= 1
while (essais != 0) & (choix != nombre) :
    print("Vous avez "+str(essais)+" essais")
    choix = int(input("Nombre choisi entre 0 et 100 ! Votre choix : "))
    is_equal(choix)
    essais -= 1

print("Le nombre était "+ str(nombre))
