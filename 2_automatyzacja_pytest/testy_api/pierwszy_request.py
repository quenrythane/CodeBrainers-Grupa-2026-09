import requests

username = "admin"
password = "admin"
base_url = "http://localhost:8000/api"


url = f"{base_url}/login"
my_headers = {}
my_payload = {
    "username": username,
    "password": password
}

response = requests.post(url, headers=my_headers, json=my_payload)

print(response.status_code)
print(response.text)
print(response)
print(type(response))

