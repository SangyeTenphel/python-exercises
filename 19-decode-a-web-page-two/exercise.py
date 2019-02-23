## The actual link I'm working with, http://content.time.com/time/magazine/article/0,9171,2005869,00.html

import requests
from bs4 import BeautifulSoup


def crawler(max_pages):
    page = 1
    while page <= max_pages:
        url = 'http://content.time.com/time/magazine/article/0,9171,2005869-'+str(page)+',00.html'
        source_code = requests.get(url)
        soup  = BeautifulSoup(source_code.text,'html.parser')

        for link in soup.findAll('p'):
            print(link.text)

        page += 1

crawler(2)
