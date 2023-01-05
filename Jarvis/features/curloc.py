import requests
from bs4 import BeautifulSoup
def getcurrentlocation():
    command="what is the temperature here"
    url=f"https://www.google.com/search?q={command}"
    r=requests.get(url)
    data=BeautifulSoup(r.text,"html.parser")
    loc=data.find("span",class_="BNeawe tAd8D AP7Wnd").text
    return loc