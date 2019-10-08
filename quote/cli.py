import argparse
import random
from quote import search

def random_search(query):
    results = search(query)
    return random.choice(results)['quote']

def cli():
    parser = argparse.ArgumentParser()
    parser.add_argument('search', nargs='?')
    args = parser.parse_args()
    return random_search(args.search)

if __name__ == '__main__':
    cli()
