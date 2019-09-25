import re
from gazpacho import get, Soup

URL = 'https://www.goodreads.com/quotes/search'
search_term = 'blake crouch'
page = 1

def make_soup(search_term, page=1):
    params = {'q': search_term, 'commit': 'Search', 'page': page}
    html = get(URL, params)
    soup = Soup(html)
    return soup

soup = make_soup(search_term, page)

soup

def parse_quote(quote_text):
    try:
        book = quote_text.find('a', {'class': 'authorOrTitle'}).text
    except AttributeError:
        book = None
    author = quote_text.find('span', {'class': 'authorOrTitle'}).text.replace(',', '')
    print(quote_text.text)
    quote = re.search('(?<=“)(.*?)(?=”)', quote_text.text).group(0)
    return {'author': author, 'book': book, 'quote': quote}

def get_quotes(soup):
    quotes = []
    for quote_text in soup.find('div', {'class': 'quoteText'}):
        quote = parse_quote(quote_text)
        quotes.append(quote)
    return quotes

get_quotes(soup)

def goodquotes(search_term):
    soup = _make_soup(search_term)
    pages = _count_pages(soup)
    all_quotes = []
    for page in range(1, pages + 1):
        soup = _make_soup(search_term, page=page)
        quotes = _get_quotes(soup)
        all_quotes.extend(quotes)
    return all_quotes
