from matplotlib.font_manager import json_dump, json_load
import requests
from bs4 import BeautifulSoup
import networkx as nx
from collections import Counter
import matplotlib.pyplot as plt
from pysondb import db
import pydot
from networkx.drawing.nx_pydot import graphviz_layout
import json 

a=db.getDb("api_text/WikiScraping.json")

def wikiScraping():

    urlvar = input("écris l'url  :").lower()

    url = 'https://fr.wikipedia.org/wiki/' + urlvar

    response = requests.get(url)

    wikiP = []

    if response.ok: 

        if a.getByQuery({'name' : urlvar}) == False or len(a.getByQuery({'name' : urlvar})) == 0:
            soup = BeautifulSoup(response.text , 'lxml')
            
            wikiWeb = soup.find("div", {"class":"mw-parser-output"}).findAll('p')

            #On récupère le text brut
            wikiP = [ i.text for i in wikiWeb ]

            
            scrapSplit = [ s.split() for s in  wikiP ]

            scrapWord = [ item for sublist in scrapSplit for item in sublist] 

            scrapCount = Counter(scrapWord)

            a.add({"name":urlvar,"count":scrapCount,"tag" : "sans tag"})

            print(a.getByQuery({"count" :{ "Pour" : 3}}))
        else:
            print("Le nom de la recherche existe déjà ou l'entrée est vide")
    else:
        print("l'url que t'as mis est pas juste ")


# wikiScraping()

# print(a.reSearch("Pour" , "3"))
print(a.dumps())
