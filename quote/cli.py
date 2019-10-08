import argparse
import random
from quote import search

def random_search(query):
    '''Randomly return one quote result'''
    results = search(query)
    random_quote = random.choice(results)['quote']
    return random_quote

def colour(string):
    '''Paint it red!'''
    string = f"\033[31m{string}\033[0m"
    return string

def cli():
    '''Randomly deliver a quote based on a search term

    Example:

    ```
    >>> max@mbp$ quote 'alain de botton'
    People only get really interesting when they start to rattle the bars of their cages.
    ```
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('search', nargs='?')
    args = parser.parse_args()
    random_quote = random_search(args.search)
    random_quote = colour(random_quote)
    return random_quote

if __name__ == '__main__':
    cli()
