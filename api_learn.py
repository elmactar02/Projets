import requests, datetime as dt

paramts = {
    "lat": 48.856613,
    "lng": 2.352222,
    "formatted": 0
}
reponse = requests.get(url="https://api.sunrise-sunset.org/json",params= paramts)
reponse.raise_for_status()

data = reponse.json()
print(data["results"]["sunrise"].split("T")[1].split(":"))
print(data["results"]["sunset"])