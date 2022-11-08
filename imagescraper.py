import requests
from bs4 import BeautifulSoup
import urllib.request
import os


def getdata(url):
    r = requests.get(url)
    return r.text


os.mkdir('media')
os.chdir('media')
htmldata = getdata("https://github.com/Code-Institute-Solutions/boutique_ado_v1/tree/bf096a773ea7e32253e20f58c1d6139317f681be/media")
soup = BeautifulSoup(htmldata, 'html.parser')
for item in soup.find_all('a'):
    link = 'https://raw.githubusercontent.com/Code-Institute-Solutions/boutique_ado_v1/bf096a773ea7e32253e20f58c1d6139317f681be/media/' + item['href'][-23:]
    name = item['href'][-23:]
    if item['href'][-3:] == 'jpg':
        print(name, link)
        with open(name.replace(' ', '-').replace('/', ''), 'wb') as f:
            im = requests.get(link)
            f.write(im.content)
