import re
from typing import Dict, List, Optional
import warnings

from gazpacho import Soup

URL = "https://www.goodreads.com/quotes/search"


def _make_soup(query: str, page: int = 1) -> Soup:
    params = {"q": query, "commit": "Search", "page": page}
    soup = Soup.get(URL, params)
    return soup


def _parse_quote(quote_text: Soup, exis_quotes=None) -> Dict[str, str]:
    """
    :param quote_text: soup object which contains quotes
    :param exis_quotes: existing quotes. if the quote is present in these, quote is not returned
    :return: quote if there is a quote and it is not present in exis_quotes, else False
    """
    exis_quotes = exis_quotes or []
    b = quote_text.find("a", {"class": "authorOrTitle"}, mode="first")
    a = quote_text.find("span", {"class": "authorOrTitle"}, mode="first")
    q = re.search("(?<=“)(.*?)(?=”)", quote_text.strip())
    quote_ = "" if not q else q.group(0)
    if quote_ in exis_quotes:
        warnings.warn("quote already exists: {}".format(quote_))
        return False
    return {
        "author": "" if not isinstance(a, Soup) else a.text.replace(",", ""),
        "book": "" if not isinstance(b, Soup) else b.text,
        "quote": quote_,
    }


def _get_page_quotes(soup: Soup, exis_quotes=None) -> List[Dict[str, str]]:
    """
    get all quotes from a page
    :param soup: soup object
    :param exis_quotes: existing quotes. if the quote is present in these, quote is not returned
    :return: list of quotes
    """
    quotes = []
    quote_texts = soup.find("div", {"class": "quoteText"}, mode="all")
    assert isinstance(quote_texts, list)
    for quote_text in quote_texts:
        quote = _parse_quote(quote_text, exis_quotes=exis_quotes)
        quotes.append(quote)
    return quotes


def _get_page_quotes_tags(soup: Soup, get_tags, get_likes, length, exis_quotes=None):
    """
    get quotes, tags and likes corresponding to each quote form a page
    :param soup:
    :param get_tags: True if you want to get the tags along with quote
    :param get_likes: True if you want to get the likes along with quote
    :param length: the maximum length a quote can be
    :param exis_quotes: existing quotes. if the quote is present in these, quote is not returned
    :return: return quotes from a goodreads page with tags and likes if requested
    """
    quotes_ = soup.find("div", {"class": "quoteDetails"}, mode="all")
    if not quotes_:
        return False
    quotes = []
    for qt in quotes_:
        quote_text = qt.find("div", {"class": "quoteText"}, mode="first")
        quote = _parse_quote(quote_text, exis_quotes=exis_quotes)
        if quote:
            if get_tags:
                if qt.find("div", {"class": "greyText smallText left"}, mode="first"):  # there are quotes with no tags.
                    tags_ = qt.find("div", {"class": "greyText smallText left"}, mode="first").find("a")
                    tags_ = tags_ if isinstance(tags_, list) else [tags_]
                    tags = [x.text for x in tags_]
                    quote.update({"tags": tags})
                else:
                    quote.update({"tags": []})
            if get_likes:
                quote.update({"likes": int(qt.find("a", {"class": "smallText"}).text.split(" ")[0])})
            if length and (len(quote.get("quote", "")) > length):
                continue
            else:
                quotes.append(quote)
    return quotes


def quote(search: str, limit: int = 20, get_tags=False, get_likes=False, length=800, skip_pages=0, verbose=False, exis_quotes=None) -> \
        Optional[List[Dict[str, str]]]:
    """
    Retrieve quotes from Goodreads

    Params:

    :param search: Author and/or book
    :param limit: Number of quotes to return
    :param get_tags: True/False to get tags corresponding to the quote
    :param get_likes: True/False to get likes corresponding to the quote
    :param length: maximum length a quote can be. default: 800 characters
    :param skip_pages: skip the first n pages while looking for quotes on goodreads
    :param verbose:
    Example:

    ```
    from quote import quote
    quote('shakespeare', limit=2)

    # [{'author': 'William Shakespeare',
    # 'book': 'As You Like It',
    # 'quote': 'The fool doth think he is wise, but the wise man knows himself to be a fool.'},
    # {'author': 'William Shakespeare',
    # 'book': "All's Well That Ends Well",
    # 'quote': 'Love all, trust a few, do wrong to none.'}]
    ```
    """
    page = skip_pages + 1
    quotes: List[Dict[str, str]] = []
    while len(quotes) < limit:
        try:
            soup = _make_soup(search, page=page)
            page_quotes = _get_page_quotes_tags(soup, get_tags, get_likes, length,exis_quotes=exis_quotes)
            if page_quotes == False:
                warnings.warn("Did not generate required amount of quotes. Num quotes: {}".format(len(quotes)))
                return quotes
            else:
                quotes.extend(page_quotes)
            if not soup.find("div", {"style": "float: right"}).text:  # type: ignore
                break
            if verbose:
                print("=========page {}, {} quotes for {}".format(page, len(quotes), search))
            page += 1
        except Exception as e:
            print(e)
            return quotes

    return quotes[:limit]
