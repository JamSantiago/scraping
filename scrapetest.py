from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib.error import  HTTPError

def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(),"html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title

title = getTitle("http://pythonscraping.com/pages/page1.html")

#http://pythonscraping.com/pages/page1.html

if (title == None):
    print("Título não foi encontrado")
else:
    print(title)
