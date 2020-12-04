import argparse
import itertools
import random
import threading
import time
from textwrap import shorten, wrap
from typing import Optional

from .quote import quote
from .spinner import Spinner


def random_search(search: str) -> Optional[str]:
    """\
    Return one random quote result from a search

    Params:

    - search: term
    """
    results = quote(search)
    if not results:
        return ""
    random_quote = random.choice(results)["quote"]
    wrapped_quote = "\n".join(
        wrap(shorten(random_quote, 280 - 4, placeholder="..."), 70)
    )
    return wrapped_quote


def colour(string: str) -> str:
    """\
    Paint it green!
    """
    string = f"\033[32m{string}\033[0m"
    return string


def cli() -> str:
    """\
    Retrieve a random quote from Goodreads

    Examples:

    ```
    >>> max@mbp % quote 'alain de botton'
    People only get really interesting when they start to rattle the bars of their cages.

    >>> max@mbp % quote shakespeare
    Though she be but little, she is fierce!
    ```
    """
    parser = argparse.ArgumentParser()
    parser.add_argument("search", nargs="?")
    args = parser.parse_args()
    spinner = Spinner()
    spinner.start()
    random_quote = random_search(args.search)
    spinner.stop()
    if not random_quote:
        return ""
    return colour(random_quote)


if __name__ == "__main__":
    cli()
