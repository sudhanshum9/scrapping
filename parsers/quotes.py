from locators.quotesloactor import  Quotelocators

class QuotesParser:
    """
    given one of the specific quotes divs,find out the data about
    the quotes (quotes content,author,tags)
    """
    def __init__(self,parent):
        self.parent= parent
    def __repr__(self):
        return f'<Quote {self.content},by {self.author}>'
    @property
    def content(self):
        locator=Quotelocators.CONTENT
        return self.parent.select_one(locator).string

    @property
    def author(self):
        locator=Quotelocators.AUTHOR
        return self.parent.select_one(locator).string

    @property
    def tags(self):
        locator=Quotelocators.TAGS
        return [e for e in self.parent.select_one(locator)]
