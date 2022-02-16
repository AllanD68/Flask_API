#%%
import requests


BASE = "http://127.0.0.1:5000/"
#%%
my_test=["naruto","dragon ball","one piece","bleach"]

for i in my_test:
    response =requests.get(BASE +"text/"+i)

#%%
response=requests.delete(BASE+'text/'+input("which one ?").replace(' ', '_'))
#%%
response =requests.delete(BASE +"All_text")
print(response.json())


# %%
response= requests.get(BASE+"text/"+input("which one ?").replace(' ', '_').lower())
print(response.json())
# %%
