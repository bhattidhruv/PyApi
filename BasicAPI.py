import requests

url = 'https://jsonplaceholder.typicode.com/todos'
response = requests.get(url)
#print(response.json())

jsonPayload = {'userId': 29, 
'id': 200, 
'title': 'Testing first Py_API', 
'completed': False}

response = requests.post(url,json = jsonPayload)
print(response.json())
itemURL = 'https://jsonplaceholder.typicode.com/todos/29'
response = requests.get(itemURL)
print(response.json())