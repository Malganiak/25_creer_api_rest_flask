import requests

url = 'http://127.0.0.1:5000/films'
response = requests.get(url)

if response.status_code == 200:
    films = response.json()
    print(films)
else:
    print(f"Erreur {response.status_code}: {response.text}")
