import requests

url = 'http://127.0.0.1:5000/bfhl'
data = {
  "data": ["A","ABcD","DOE"]
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())
