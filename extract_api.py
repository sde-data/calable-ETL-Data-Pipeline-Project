import requests
import json

url = "https://api.coindesk.com/v1/bpi/currentprice.json"

response = requests.get(url)
data = response.json()

with open("data/raw_data.json","w") as f:
    json.dump(data,f)
