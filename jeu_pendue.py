import random

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

nb_lettre = random.randint(1,8)

mot = ""

for i in range(1,nb_lettre+1):
    mot += random.choice(alphabet)

print(r"""
     _   _                                         
    | | | |                                        
    | |_| | __ _ _ __   __ _ _ __ ___   __ _ _ __ 
    |  _  |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \
    | | | | (_| | | | | (_| | | | | | | (_| | | | |
    \_| |_/\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                        __/ |                    
                       |___/                     
    """)

list_mot_lettre = []
for i in range(0,nb_lettre):
    list_mot_lettre.append("_")

def mot_lettre_to_str(list_mot_lettre):
    res = ""
    for char in list_mot_lettre:
        res += str(char)
        res += " "
    return res

def find_in_list(target,py_list) :
  indices_cibles = []
  for i in range(len(py_list)) :
    if py_list[i] == target :
      indices_cibles.append(i) 

  return indices_cibles
 
def creer_mot_avec_lettre_trouve(lettre):
        res = ""
        indx = find_in_list(lettre,mot)
        for j in indx:
            modif = str(lettre) + " "
            list_mot_lettre[j] = modif

def affich_bonhomme(nb_essai):
    if nb_essai == 6:
        print(r"""
        _______
        |/
        |
        |
        |
        |
    -----------
    """)
    elif nb_essai == 5:
        print(r"""
        _______
        |/     |
        |      O
        |      
        |
        |
    -----------
    """)
    elif nb_essai == 4:
        print(r"""
        _______
        |/     |
        |      O
        |      |
        |
        |
    -----------
    """)
    elif nb_essai == 3:
        print(r"""
        _______
        |/     |
        |      O
        |     /|
        |
        |
    -----------
    """)
    elif nb_essai == 2:
        print(r"""
        _______
        |/     |
        |      O
        |     /|\
        |     
        |
    -----------
    """)
    elif nb_essai == 1:
        print(r"""
        _______
        |/     |
        |      O
        |     /|\
        |     / 
        |
    -----------
    """)
    else :
        print(r"""
        _______
        |/     |
        |      O
        |     /|\
        |     / \
        |
    -----------
    """)

essais = 6 
while essais != 0:   
    mot_avec_lettre = mot_lettre_to_str(list_mot_lettre)
    print("Le mot à deviner : "+ mot_avec_lettre)
    lettre = input("Devines une lettre: ")

    if lettre in mot:
        creer_mot_avec_lettre_trouve(lettre)
        print("Bravo une lettre trouvé, il te reste " + str(essais) +" essais")
        affich_bonhomme(essais)
        if mot == mot_lettre_to_str(list_mot_lettre).replace(" ","") :
            print("TU AS GAGNE !")
            break
    else:
        essais -= 1
        print("Dommage il te reste "+ str(essais) + " essais")
        affich_bonhomme(essais)
        if mot == mot_lettre_to_str(list_mot_lettre).replace(" ",""):
            print("TU AS GAGNE !")
            break
if mot != mot_lettre_to_str(list_mot_lettre).replace(" ",""):   
    print("PERDU !")

