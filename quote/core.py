import re
import json
from gazpacho import get, Soup

URL = 'https://www.goodreads.com/quotes/search'

def make_soup(query, page=1):
    params = {'q': query, 'commit': 'Search', 'page': page}
    html = get(URL, params)
    soup = Soup(html)
    return soup

def parse_quote(quote_text):
    try:
        book = quote_text.find('a', {'class': 'authorOrTitle'}).text
    except AttributeError:
        book = None
    author = quote_text.find('span', {'class': 'authorOrTitle'}).text.replace(',', '')
    quote = re.search('(?<=“)(.*?)(?=”)', quote_text.text).group(0)
    return {'author': author, 'book': book, 'quote': quote}

def get_page_quotes(soup):
    quotes = []
    for quote_text in soup.find('div', {'class': 'quoteText'}):
        try:
            quote = parse_quote(quote_text)
            quotes.append(quote)
        except:
            pass
    return quotes

def search(query, limit=20):
    page = 1
    quotes = []
    while True:
        if len(quotes) > limit:
            break
        soup = make_soup(query, page=page)
        page_quotes = get_page_quotes(soup)
        if not page_quotes:
            break
        quotes.extend(page_quotes)
        page += 1
    quotes = quotes[:limit]
    return json.dumps(quotes, indent=2)
