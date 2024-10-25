import requests

url = "https://countriesnow.space/api/v0.1/countries/population"

data = {"country": "nigeria"}

response = requests.post(url, data=data)

print(response.text)