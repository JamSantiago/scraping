from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import  HTTPError
import re



def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(),"html.parser")
        bsObj.findAll(html)
    except AttributeError as e:
        return None
    return title

#title = getTitle("http://pythonscraping.com/pages/page1.html")

def getName(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html)
        nameList = bsObj.findAll("span",{"class":"green"})
        for name in nameList:
            print(name.get_text())

    except AttributeError as e:
        return None

#name = getName("http://pythonscraping.com/pages/warandpeace.html")
#http://pythonscraping.com/pages/page1.html

#if (title == None):
#    print("Título não foi encontrado")
#else:
#    print(title)

def imprimePreco():
    html = urlopen("http://www.pythonscraping.com/pages/page3.html")
    bsObj = BeautifulSoup(html)
    print(bsObj.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text)

def imprimeChild():
    html = urlopen("http://www.pythonscraping.com/pages/page3.html")
    bsObj = BeautifulSoup(html)
    for child in bsObj.find("table",{"id":"giftList"}).children:
        print(child)
def imprimeNextSiblings():
    html = urlopen("http://www.pythonscraping.com/pages/page3.html")
    bsObj = BeautifulSoup(html)
    for sibling in bsObj.find("table",{"id":"giftList"}).tr.next_siblings: #bsObj.table.tr... < código mais simples
        '''
        tags semelhantes: next_siblings, next_sibling, previous_sibling, previous_siblings
        '''
        print(sibling)
def imprimeImagens():
    html = urlopen("http://www.pythonscraping.com/pages/page3.html")
    bsObj = BeautifulSoup(html,"html.parser")
    imagens = bsObj.findAll("img",{"src":re.compile(".\.\/img\/gifts/img.*\.jpg")})
    for img in imagens:
        print(img)

def expLambda():
    html = urlopen("http://www.pythonscraping.com/pages/page3.html")
    bsObj = BeautifulSoup(html,"html.parser")
    result = bsObj.findAll(lambda tag: len(tag.attrs) == 2) #retorna tags com dois atributos
    for n in result:
        print(n)
        
expLambda()