import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

# GET
response = requests.get(url)
print("GET:", response.json())

# POST
data = {
    "title": "Hello",
    "body": "Learning API",
    "userId": 1
}

response = requests.post(
    "https://jsonplaceholder.typicode.com/posts",
    json=data
)
print("POST:", response.json())

# PUT
response = requests.put(url, json=data)
print("PUT:", response.json())

# PATCH
data = {
    "title": "New Title"
}

response = requests.patch(url, json=data)
print("PATCH:", response.json())

# DELETE
response = requests.delete(url)
print("DELETE:", response.status_code)