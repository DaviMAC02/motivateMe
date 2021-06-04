import sqlite3
import urllib.error
import ssl
from urllib.parse import urljoin
from urllib.parse import urlparse
from urllib.request import urlopen
from bs4 import BeautifulSoup


# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


conn = sqlite3.connect("quotes.sqlite")
cursor = conn.cursor()

cursor.execute('''CREATE TABLE IF NOT EXISTS Quotes
    (id INTEGER PRIMARY KEY, quote TEXT UNIQUE)''')


url = "https://crmpiperun.com/blog/frases-motivacionais/"

document = urlopen(url, context=ctx)

html = document.read()

soup_of_html = BeautifulSoup(html, "html.parser")

quotesTags = soup_of_html.findAll('h4')
quotes = []
for quote in quotesTags:
    quote = str(quote)
    if quote.endswith(")</h4>"):
        quote = quote[12:]
        quote = quote[:-5]
        quotes.append(quote)

fhand = open('../script/quotes.js', 'w', encoding='utf-8')

fhand.write('var quotesContainer = {\n "quotes":[\n')

for quote in quotes:
    print(quote)
    fhand.write("{quote:'" + quote + "'},\n")

fhand.write(']}')
