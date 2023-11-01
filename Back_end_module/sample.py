import requests

request = requests.get('http://127.0.0.1:8000/check/3729307418')

print(request.json())