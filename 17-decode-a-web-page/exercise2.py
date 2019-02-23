import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    url = 'http://toscrape.com/'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "html.parser")
    i = 1
    for heading in soup.findAll('h2'):
        title = heading.string
        print(str(i),title)
        i+=1
