import requests
import json
from bs4 import BeautifulSoup

def get_news():
    url = 'https://www.bbc.com/news'
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    headlines = soup.find('body').find_all('h3')
    unwanted = ['BBC World News TV', 'BBC World Service Radio',
                'News daily newsletter', 'Mobile app', 'Get in touch']
    ls=[]
    count=0
    for x in list(dict.fromkeys(headlines)):
        if x.text.strip() not in unwanted:
            # print(x.text.strip())
            ls.append(x.text.strip())
            count=count+1
        if count==5:
            break
    return ls