import random
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
carrac_spec = ['&','#','@','+','-','_','?','!','%']
list_concat= alphabet+ carrac_spec
print("Generateur de mot de passe aléatoire !")

nb_lettre = int(input("Combien de lettres souhaites tu ? : "))
nb_car_spe = int(input("Combien de carractères spéciaux ? "))

mdp = ""
j = 0
for i in range(0,nb_lettre):
    char = random.choice(list_concat)
    if char in carrac_spec:
        j+=1
        if j != 2:
            mdp+= char
    else:
        mdp+= char

    
print("Voici ton mot de passe aléatoire: " + mdp)

