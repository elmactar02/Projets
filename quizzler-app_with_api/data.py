import requests

reponse = requests.get(url="https://opentdb.com/api.php?amount=10&type=boolean")
reponse.raise_for_status()
question_data = reponse.json()["results"]
