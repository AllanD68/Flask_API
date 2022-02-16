from genericpath import exists
from matplotlib.font_manager import json_dump, json_load
import requests
from bs4 import BeautifulSoup
from collections import Counter
import matplotlib.pyplot as plt
import json 
import itertools
import os.path

# a=db.getDb("api_text/WikiScraping.json")



def wikiScraping(urlvar):
    urlvar=urlvar.replace(' ', '_')
    url = 'https://fr.wikipedia.org/wiki/' + urlvar

    response = requests.get(url)

    wikiP = []

    if response.ok: 

            soup = BeautifulSoup(response.text , 'lxml')
            
            wikiWeb = soup.find("div", {"class":"mw-parser-output"}).find_all('p')

            #On récupère le text brut
            wikiP = [ i.text for i in wikiWeb ]

            
            scrapSplit = [ s.split() for s in  wikiP ]

            scrapWord = [ item for sublist in scrapSplit for item in sublist] 
            
            scrapDic = dict(Counter(scrapWord))
	      
            # print(scrapDic)

            # print(type(scrapDic))

            if os.path.isfile('JsonDB/' + urlvar + '.json') == False:
                with open('JsonDB/' + urlvar + '.json', 'w') as f:
                    json.dump(scrapDic, f)
                # print("Fichier Json créé")
                return json.dumps(scrapDic)
            else:
                with open('JsonDB/' + urlvar + '.json', 'r') as f:
                    j = json.load(f)
                    # print("Cette recherche est déjà en mémoire")
                    return j

    else:
        return False
        





