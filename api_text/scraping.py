from turtle import title
import requests
from bs4 import BeautifulSoup

urlvar = input("écris l'url  :")

url = 'https://fr.wikipedia.org/wiki/' + urlvar


response = requests.get(url)

wikiP = []

if response.ok:
    soup = BeautifulSoup(response.text , 'lxml')
    # title = soup.find('title')
    # print('title.text')
    # wikiP = soup.find("tr", {"class": "ranking-list"})
    
    wikiWeb = soup.find("div", {"class":"mw-parser-output"}).findAll('p')

    wikiP = [ i.text for i in wikiWeb ]


    ScrapWord = [ s.split() for s in  wikiP ]



    for n in range(len(ScrapWord)):
        print(ScrapWord[n])
else:
    print("l'url que t'as mis est pas juste ")




    # print(wikiP)
    # di-ib clearfix