import random
print(r"""
     ____  _            _     _            _    
    | __ )| | __ _  ___| | __(_) __ _  ___| | __
    |  _ \| |/ _` |/ __| |/ /| |/ _` |/ __| |/ /
    | |_) | | (_| | (__|   < | | (_| | (__|   < 
    |____/|_|\__,_|\___|_|\_\|_|\__,_|\___|_|\_\

        .-------.
        | A   ^ |
        |  ♠  |  
        |     v |
        '-------'
    """)

print("Bienvenue dans le monde du blackjack !")
oui_ou_non = input("Souhaitez vous jouer une partie ? (y/n)  ")
tableau_carte = [11,2,3,4,5,6,7,8,9,10,10,10,10]
pioches = [random.choice(tableau_carte),random.choice(tableau_carte)]
pioches_robot_visible = [random.choice(tableau_carte)]
pioches_robot = pioches_robot_visible
while ((oui_ou_non == 'y' and sum(pioches) <= 21) | (sum(pioches) < 12)):
    print("Voici ta pioche "+ str(pioches)+" = "+ str(sum(pioches)))
    print("Voici la pioche de la machine "+str(pioches_robot_visible))
    oui_ou_non = input("Souhaitez vous prendre une carte ? (y/n)  ")
    if oui_ou_non == 'y':
        ajout = random.choice(tableau_carte)
        pioches.append(ajout)
        if( sum(pioches) > 21 ) & (ajout == 11) :
            pioches[-1]= 1

if sum(pioches) <= 21:
    while(sum(pioches_robot)<12):
        ajout_robot = random.choice(tableau_carte)
        pioches_robot.append(ajout_robot)
        if( sum(pioches_robot) > 21 ) & (ajout_robot == 11) :
                pioches_robot[-1]= 1
        while (sum(pioches_robot) >= 12 & sum(pioches_robot) != 21):
            action = random.randint(0,2)
            if action == 0:
                ajout_robot = random.choice(tableau_carte)
                pioches_robot.append(ajout_robot)
                if( sum(pioches_robot) > 21 ) & (ajout_robot == 11) :
                    pioches_robot[-1]= 1
                else:
                    break

print("Votre pioche final est "+ str(pioches)+" ="+str(sum(pioches)))
print("La pioche final de la machine est "+ str(pioches_robot)+" ="+ str(sum(pioches_robot)))
if(sum(pioches) > 21):
    print("Vous avez perdu !")
elif (sum(pioches_robot) > 21):
    print("Vous avez gagnez !")
elif (sum(pioches)< sum(pioches_robot) ) :
    print("Vous avez perdu !")
elif sum(pioches) > sum(pioches_robot):
    print("Vous avez gagné !")
elif sum(pioches) == sum(pioches_robot):
    print("Egalité")