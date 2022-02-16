import requests

BASE = "http://127.0.0.1:5000/"

# my_test=["france","isaac newton","jean claude vandamme"]
# print(my_test[0])
# for each in my_test:
# response =requests.get(BASE +"text/"+my_test[0])
# print(response.json())
response =requests.delete(BASE +"text/france")
print(response.json())