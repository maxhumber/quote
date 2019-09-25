from quote.newsoup import Soup, get

url = 'https://www.goodreads.com/quotes/search?commit=Search&page=2&q=blake+crouch'
html = get(url)

soup = Soup(html)
soup.find('div', {'class': 'quoteText'})


data = [l.strip() for l in parser.container]
data = [l for l in data if l != '' and not l.startswith('//<')]
data = '\n'.join(data).split('“')[1:]
data


def _make_soup(search_term, page=1):
    payload = {'q': search_term, 'commit': 'Search', 'page': page}
    response = requests.get(url, params=payload)
    html = response.text
    soup = BeautifulSoup(html, 'lxml')
    [script.decompose() for script in soup.find_all('script')]
    return soup

def _count_pages(soup):
    try:
        pages = soup.find_all('div', attrs={'style': 'float: right'})[0]
        total_pages = int([a.text for a in pages.find_all('a')][-2])
    except IndexError:
        total_pages = 1
    return total_pages

def _parse_quote(quote_text):
    try:
        book = quote_text.find('a', attrs={'class': 'authorOrTitle'}).text
    except AttributeError:
        book = None
    author = quote_text.select('span.authorOrTitle')[0].text.strip().replace(',', '')
    quote = re.search('(?<=“)(.*?)(?=”)', quote_text.text.strip()).group(0)
    return {'author': author, 'book': book, 'quote': quote}

def _get_quotes(soup):
    quotes = []
    for quote_text in soup.select('.quoteText'):
        quote = _parse_quote(quote_text)
        quotes.append(quote)
    return quotes

def goodquotes(search_term):
    soup = _make_soup(search_term)
    pages = _count_pages(soup)
    all_quotes = []
    for page in range(1, pages + 1):
        soup = _make_soup(search_term, page=page)
        quotes = _get_quotes(soup)
        all_quotes.extend(quotes)
    return all_quotes
