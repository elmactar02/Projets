alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']

print(r"""
      ____ ____  _____    _    ____  
     / ___|  _ \| ____|  / \  |  _ \ 
    | |   | | | |  _|   / _ \ | | | |
    | |___| |_| | |___ / ___ \| |_| |
     \____|____/|_____/_/   \_\____/ 
                                       
    """)

def list_to_str(new_list_char_mot):
    nouveau_mot = ""
    for char in new_list_char_mot:
        nouveau_mot += char
    return nouveau_mot
def encoder(list_char_mot,alphabet,saut):
    new_list_char_mot = []
    for char in list_char_mot:
        new_list_char_mot.append(alphabet[alphabet.index(char) + saut])
    return new_list_char_mot
def decoder(list_char_mot,alphabet,saut):
    new_list_char_mot = []
    for char in list_char_mot:
        new_list_char_mot.append(alphabet[alphabet.index(char) - saut])
    return new_list_char_mot
continuer = 1 
while continuer == 1 :    
    choix = str(input("Tapez (encode) pour encoder et (decode) pour decoder: "))
    saut = int(input("De combien est le shift ? "))
    list_char_mot = list(str(input("Saisissez votre mot : ")))
    new_list_char_mot = []
    if choix == "encode":
        new_list_char_mot = encoder(list_char_mot,alphabet,saut)
        nouveau_mot = list_to_str(new_list_char_mot)
        print("Voici vôtre encodage: " + nouveau_mot)
    else:
        new_list_char_mot = decoder(list_char_mot,alphabet,saut)
        nouveau_mot = list_to_str(new_list_char_mot)
        print("Voici vôtre decodage: " + nouveau_mot)

    continuer = int(input("Voulez vous continuer (1) ou arreter (0) : "))