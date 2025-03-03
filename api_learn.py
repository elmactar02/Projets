import requests, datetime as dt
from twilio.rest import Client
import os
apikey = os.environ.get("apikey")
print(apikey)
paramts = {
    "lat": 48.963677,
    "lon": 2.339912,
    "appid": os.environ.get("apikey"),
    "cnt": 7,
}
reponse = requests.get("https://api.openweathermap.org/data/2.5/forecast",params= paramts)
reponse.raise_for_status()

data = reponse.json()
my_list = [item["weather"][0]["id"] for item in data["list"] if item["weather"][0]["id"] < 700]

if my_list.__len__() > 0:

    account_sid=os.environ.get("account_sid")
    auth_token=os.environ.get("auth_token")
    client = Client(account_sid, auth_token)

    message = client.messages.create(
    from_='+14705673996',
    body='Take an ambrella today it will rain ☔',
    to='...'
    )

    print(message.status)