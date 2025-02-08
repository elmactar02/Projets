personnalités = [
    {
        'name': 'Lionnel Messi',
        'followers': 4000020,
        'description': 'Football player',
    },
    {
        'name': 'Cristiano Ronaldo',
        'followers': 5500000,
        'description': 'Football player',
    },
    {
        'name': 'Neymar Jr',
        'followers': 3050000,
        'description': 'Football player',
    },
    {
        'name': 'Zlatan Ibrahimovic',
        'followers': 2005000,
        'description': 'Football player',
    },
    {
        'name': 'Sergio Ramos',
        'followers': 1500080,
        'description': 'Football player',
    },
    {
        'name': 'Sergio Busquets',
        'followers': 1040000,
        'description': 'Football player',
    },
    {
        'name': 'Sergio Aguero',
        'followers': 1000500,
        'description': 'Football player',
    },
    {
        'name': 'Novak Djockovic',
        'followers': 1700000,
        'description': 'Tennis player',
    },
    {
        'name': 'Rafael Nadal',
        'followers': 1500000,
        'description': 'Tennis player',
    },
    {
        'name': 'Roger Federer',
        'followers': 2000000,
        'description': 'Tennis player',
    },
    {
        'name': 'Nick kyrgios',
        'followers': 900000,
        'description': 'Tennis player',
    },
    {
        'name': 'Lewis Hamilton',
        'followers': 1550000,
        'description': 'F1 driver',
    },
    {
        'name': 'Tiger Wood',
        'followers': 1600000,
        'description': 'Golf player',
    }
]
import random, os , time
score = 0
print("========================================================================")
print("                            BIENVENUE                                   ")
print("========================================================================")

a_perdu = False
time.sleep(5)
while not a_perdu:
    os.system('cls')
    print("Your score is "+str(score))
    print("                  Who is the most popular ?  Between                    ")
    list_len = len(personnalités) - 1
    first = random.randint(0,list_len)
    second = random.randint(0,list_len)

    print(personnalités[first]['name']+"  VS  "+ personnalités[second]['name'])
    choix = input("A or B : ")
    if personnalités[first]['followers'] < personnalités[second]['followers'] :
        most_popular = personnalités[second]
    else:
        most_popular = personnalités[first]

    if choix == 'A':
        if most_popular == personnalités[first]:
            score +=1
        else:
            a_perdu = True
    else:
        if most_popular == personnalités[second]:
            score +=1
        else:
            a_perdu = True

print("Votre score final est de "+str(score))