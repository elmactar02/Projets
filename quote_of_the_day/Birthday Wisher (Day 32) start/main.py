import random
import smtplib 
import datetime as dt

email = ""
mdp= ""
day_of_week_today = dt.datetime.now().weekday()
list_quotes = []
try:
    with open("quotes.txt") as file:
        list_quotes = file.readlines()
except:
    raise FileNotFoundError
else:
    if day_of_week_today == 4:
        quote_of_day = random.choice(list_quotes)
        with smtplib.SMTP("smtp.gmail.com",port=587) as connexion:
            connexion.starttls()
            connexion.login(user=email,password=mdp)
            connexion.sendmail(from_addr=email,to_addrs="",
                            msg=f"Subject:Motivation of the day\n\n {quote_of_day}")

