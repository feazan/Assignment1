import urllib.request
from bs4 import BeautifulSoup

articles = open("top10articles.txt", "w")

page = urllib.request.urlopen("https://finance.google.com/finance/market_news")
bs = BeautifulSoup(page, "html.parser")
spans = bs.findAll('span', attrs={'class': 'name'})
src = bs.findAll('span', attrs={'class': 'src'})
date = bs.findAll('span', attrs={'class': 'date'})

for i in range(0,10):
    articles.write(spans[i].text.strip() + "," + src[i].text + "," + date[i].text + "\n")

# Think I need to return this as a list