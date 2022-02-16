from matplotlib.font_manager import json_dump, json_load
import requests
from bs4 import BeautifulSoup
from collections import Counter
import matplotlib.pyplot as plt
import json 
import itertools

# a=db.getDb("api_text/WikiScraping.json")



def wikiScraping():

    urlvar = input("écris l'url  :").lower()

    url = 'https://fr.wikipedia.org/wiki/' + urlvar

    response = requests.get(url)

    wikiP = []

    if response.ok: 

        # if a.getByQuery({'name' : urlvar}) == False or len(a.getByQuery({'name' : urlvar})) == 0:
            soup = BeautifulSoup(response.text , 'lxml')
            
            wikiWeb = soup.find("div", {"class":"mw-parser-output"}).find_all('p')

            #On récupère le text brut
            wikiP = [ i.text for i in wikiWeb ]

            
            scrapSplit = [ s.split() for s in  wikiP ]

            scrapWord = [ item for sublist in scrapSplit for item in sublist] 
            
            scrapDic = dict(Counter(scrapWord))
	      
            print(scrapDic)

            print(type(scrapDic))

            with open('JsonDB/' + urlvar + '.json', 'w') as f:
                json.dump(scrapDic, f)

            # testDic = json.loads(urlvar + '.json'))

           

        # else:
        #     print("Le nom de la recherche existe déjà ou l'entrée est vide")
    else:
        print("l'url que t'as mis est pas juste ")


wikiScraping()


