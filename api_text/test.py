import requests

BASE = "http://127.0.0.1:5000/"

# my_test=["naruto","dragon ball","one piece"]

# for i in my_test:
#     response =requests.get(BASE +"text/"+i)
#     print(response.json())


response =requests.delete(BASE +"All_text")
print(response.json())

