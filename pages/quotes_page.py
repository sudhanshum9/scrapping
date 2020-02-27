from bs4 import BeautifulSoup

from locators.quotes_page_locator import Quotepagelocator
from parsers.quotes import QuotesParser


class QuotesPage:
    def __init__(self,page):
        self.soup= BeautifulSoup(page,"html.parser")

    @property
    def quotes(self):
         locator=Quotepagelocator.QUOTE
         quote_tags=self.soup.select(locator)
         return [QuotesParser(e) for e in quote_tags]