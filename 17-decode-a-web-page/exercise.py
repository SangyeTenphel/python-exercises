import requests
from bs4 import BeautifulSoup

def web_crawler():
    #This site doesn't allow web scraping anymore so I have done this in another site.
    url = 'https://www.nytimes.com'
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,'html.parser')
    for link in soup.findAll('span',{'class':'balancedHeadline'}):
        title = link.string
        print(title)

web_crawler()

