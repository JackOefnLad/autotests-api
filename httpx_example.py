import httpx
import os

os.environ["NO_PROXY"] = "*"
# ----GET
# response = httpx.get("https://jsonplaceholder.typicode.com/todos/1")

# print(response.status_code)
# print(response.json())

#----POST
# data = {
#     "login":"test",
#     "password":"test"
# }

# response = httpx.post('http://192.168.185.23:4000/login', json=data)

# print(response.status_code)
# print(response.json())

# #----Post с form-data
# data = {"username": "test", "password":"123456"}
# response = httpx.post("https://httpbin.org/post", data=data)

# print(response.status_code)
# #----Добавление заголовков к запросам
# headers={"Authorization": "Bearer token"}
# response = httpx.get("https://httpbin.org/get", headers=headers)
# #----Query парамс

# response = httpx.get('https://jsonplaceholder.typicode.com/todos?userId=1') #Demo

# params = {"userId":"1"}
# response = httpx.get('https://jsonplaceholder.typicode.com/todos', params = params)

# #----File
# files = {"file": ("example.txt", open("example.txt", "rb"))}

# response = httpx.post("https://httpbin.org/post", files=files)

# print(response.json())  # Ответ с данными о загруженном файле 

# #----withClient
# with httpx.Client() as client:
#     response1 = client.get('https://jsonplaceholder.typicode.com/todos/1')
#     response2 = client.get('https://jsonplaceholder.typicode.com/todos/2')

# print(response1.json())
# print(response2.json())

# #----Client + headers
# client = httpx.Client(headers={"Authorization":"Bearer"})
# response = client.get("https://httpbin.org/get")
# print(response.json())

try:
    response = httpx.get("https://jsonplaceholder.typicode.com/123213")
    print(response.status_code)
except httpx.HTTPStatusError as e:
    print(f"Ошибка запроса: {e}")