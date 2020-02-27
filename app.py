import requests
from pages.quotes_page import QuotesPage

page_content=requests.get('http://quotes.toscrape.com').content
page=QuotesPage(page_content)

for qoute in page.quotes:
    print(qoute)

