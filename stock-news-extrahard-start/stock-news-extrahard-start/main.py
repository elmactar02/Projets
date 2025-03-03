STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
import requests,smtplib,datetime

email = ""
mdp= ""
my_addr = ""
difference_percentage: int
fev_28 = str(datetime.date.today() - datetime.timedelta(days=3))
fev_27 = str(datetime.date.today() - datetime.timedelta(days=4))


## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
parameters1 = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "TSLA" ,
    "apikey": "A1T1HFZHN9AX8DCV",
    }
parameters2 = {
    "function": "NEWS_SENTIMENT",
    "tickers": "TSLA" ,
    "apikey": "A1T1HFZHN9AX8DCV",
    }

reponse = requests.get(url="https://www.alphavantage.co/query",params=parameters1)
reponse.raise_for_status()
data = reponse.json()
prix_hier = float(data["Time Series (Daily)"][fev_28]["4. close"])
#prix_avant_hier = float(data["Time Series (Daily)"][fev_27]["4. close"])
prix_avant_hier = 210.5
difference_percentage = ( (prix_hier - prix_avant_hier) / prix_hier )*100
difference_percentage_absolue = abs(difference_percentage)

## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 
if difference_percentage_absolue > 5:
    reponse2 = requests.get(url="https://www.alphavantage.co/query",params=parameters2)
    reponse2.raise_for_status()
    data_news = reponse2.json()["feed"][:3]

    modele1 = f"Subject:TSLA: Up {difference_percentage} \n\n Headline:{data_news[0]["title"]}\nBrief: {data_news[0]["summary"]}"
    modele2 = f"Subject:TSLA: Down {difference_percentage} \n Headline:{data_news[0]["title"]}\nBrief: {data_news[0]["summary"]}"
    if difference_percentage > 0 :
            message = modele1
    else:
            message = modele2
## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 
    with smtplib.SMTP("smtp.gmail.com",port=587) as connexion:
                connexion.starttls()
                connexion.login(user=email,password=mdp)
                connexion.sendmail(from_addr=email,to_addrs=my_addr,
                               msg=message)

#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

