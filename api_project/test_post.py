import requests

url = "http://127.0.0.1:8000/api/echo/"
payload = {"name": "Ali", "age": 25}


response = requests.post(url, json=payload)

print("----- Status -----")
print(response.status_code)

print("----- Headers -----")
print(response.headers)

print("----- JSON -----")
print(response.json())
