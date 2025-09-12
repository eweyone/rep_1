import requests

url = "http://127.0.0.1:8000/predict_post"
data = {
    "total_square": 50.0,
    "floor": 5
}

response = requests.post(url, json=data)

print(response.json())