import argparse
import itertools
import random
import threading
import time

from .core import search
from .spinner import Spinner

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
    spinner = Spinner()
    spinner.start()
    random_quote = colour(random_search(args.search))
    spinner.stop()
    return random_quote

if __name__ == '__main__':
    cli()
