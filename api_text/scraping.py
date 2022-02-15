import requests
from bs4 import BeautifulSoup
import networkx as nx
from collections import Counter
import matplotlib.pyplot as plt
import pydot
from networkx.drawing.nx_pydot import graphviz_layout

# urlvar = input("écris l'url  :")

# url = 'https://fr.wikipedia.org/wiki/' + urlvar

url = 'https://fr.wikipedia.org/wiki/'

response = requests.get(url)

wikiP = []

if response.ok:

    soup = BeautifulSoup(response.text , 'lxml')
    
    wikiWeb = soup.find("div", {"class":"mw-parser-output"}).findAll('p')

    wikiP = [ i.text for i in wikiWeb ]

    scrapSplit = [ s.split() for s in  wikiP ]

    scrapWord = [ item for sublist in scrapSplit for item in sublist] 

    scrapCount = Counter(scrapWord)

    print(scrapCount)


else:
    print("l'url que t'as mis est pas juste ")


# -------------------------------------------

