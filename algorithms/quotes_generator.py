import sqlite3
import ssl
from urllib.request import Request, urlopen
from urllib.request import urlopen
from bs4 import BeautifulSoup


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


class Quote:
    def __init__(self, quote_text, quote_author):
        self.quote_text = quote_text
        self.quote_author = quote_author




req = Request(
    url='https://www.pensador.com/365_frases_motivacionais/', 
    headers={'User-Agent': 'Mozilla/5.0'}
)

document = urlopen(req, context=ctx)

html = document.read()

soup_of_html = BeautifulSoup(html, "html.parser")

quotesTags = soup_of_html.find_all('blockquote')
quotes_block = []
for quote in quotesTags:
    quotes_block.append(quote.find_all('p'))


quotes = []

for quote in quotes_block:
    if(len(quote) > 1):
        quote_text = str(quote[0])
        quote_text = quote_text[:-4]
        quote_text = quote_text[3:]
        quote_author = str(quote[1])
        quote_author = quote_author[:-4]
        quote_author = quote_author[17:]
        quotes.append(Quote(quote_text, quote_author))

    

for quote in quotes:
    print(quote.quote_author)    
