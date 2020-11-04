import requests

url = 'https://jsonplaceholder.typicode.com/todos'

print('working of HTTP GET request ')
print()

#syntax for HTTP GET
response = requests.get(url)
print(response.json())

print()
print('***********************************************************')
print()

print('wokring of HTTP POST Rquest')
print()

#creating json Payload to be added in the data server
jsonPayload = {'userId': 29, 
'id': 200, 
'title': 'Testing first Py_API', 
'completed': False}

#syntax for HTTP POST
response = requests.post(url,json = jsonPayload)
print(response.json())

print()
print('***********************************************************')
print()

print('wokring of HTTP PUT Rquest')
print()

#get a specific item
itemURL = 'https://jsonplaceholder.typicode.com/todos/29'
response = requests.get(itemURL)
print('before PUT')
print(response.json())

putPayload = {
'userId': 2, 
'id': 29, 
'title': 'has been modified', 
'completed': False
}

putResponse = requests.put(itemURL,json = putPayload)
print('after PUT')
print(putResponse.json())

print()
print('***********************************************************')
print()

print('wokring of HTTP Delete Rquest')
print()

deleteResponse = requests.delete(itemURL)
print(deleteResponse.json())
#print(requests.get(itemURL).json())

