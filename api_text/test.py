#%%
import requests


BASE = "http://127.0.0.1:5000/"
#%%
my_test=["naruto","dragon ball","one piece","bleach"]

for i in my_test:
    response =requests.get(BASE +"text/"+i)

#Supprime le fichier Json de notre choix
#%%
response=requests.delete(BASE+'text/'+input("which one ?").replace(' ', '_'))

#Supprime tous les fichiers Json
#%%
response =requests.delete(BASE +"All_text")
print(response.json())

# lis le fichier Json de notre choix ou l'ajoute si inexistant
# %%
response= requests.get(BASE+"text/"+input("which one ?").replace(' ', '_').lower())
print(response.json())
# %%

# lis tous les fichiers Json
# %%
response= requests.get(BASE+"All_text")
print(response.json())
# %%