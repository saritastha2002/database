import requests
6/-986+7



url="http://127.0.0.1:8000/article/edit/1"/-
response = requests.get(url)

print(response.json())