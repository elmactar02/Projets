##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import datetime as dt
import random,sys
import pandas,smtplib

email = ""
mdp= ""
date_today = dt.datetime.now()
day_today = dt.datetime.now().day
month_today = dt.datetime.now().month
donnees_birthdays = pandas.read_csv("birthdays.csv")
try:
    person_to_wish = donnees_birthdays[(day_today == donnees_birthdays["day"]) & (month_today == donnees_birthdays["month"])]
except:
    print("Nobody to wish today !")
else:
    for (index,item) in person_to_wish.iterrows() :
        list_lettre = ["letter_1.txt","letter_2.txt","letter_3.txt"]
        choix = random.choice(list_lettre)
        with open(f"letter_templates/{choix}") as file:
            message = file.read().replace("[NAME]",str(item["name"]))

        with smtplib.SMTP("smtp.gmail.com",port=587) as connexion:
                connexion.starttls()
                connexion.login(user=email,password=mdp)
                connexion.sendmail(from_addr=email,to_addrs=item["email"],
                               msg=message)




