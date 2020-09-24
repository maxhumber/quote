<h3 align="center">
  <img src="https://raw.githubusercontent.com/maxhumber/quote/master/quote.png" height="300px" alt="quote">
</h3>
<p align="center">
  <a href="https://github.com/maxhumber/gazpacho"><img alt="gazpacho" src="https://img.shields.io/badge/scraper-gazpacho-C6422C"></a>
  <a href="https://travis-ci.org/maxhumber/quote"><img alt="Travis" src="https://img.shields.io/travis/maxhumber/quote.svg"></a>
  <a href="https://pypi.python.org/pypi/quote"><img alt="PyPI" src="https://img.shields.io/pypi/v/quote.svg"></a>
  <a href="https://pepy.tech/project/quote"><img alt="Downloads" src="https://pepy.tech/badge/quote"></a>
</p>




#### About

`quote` is a python wrapper for the Goodreads Quote API, powered by [gazpacho](https://github.com/maxhumber/gazpacho).



#### Quickstart

`quote` is simple to use:

```python
from quote import quote

search = 'Jasper Fforde'
result = quote(search, limit=2)
print(result)

# [{'author': 'Jasper Fforde',
#   'book': 'Something Rotten',
#   'quote': 'If the real world were a book, it would never find a publisher. Overlong, detailed to the point of distraction-and ultimately, without a major resolution.'},
#  {'author': 'Jasper Fforde',
#   'book': 'The Well of Lost Plots',
#   'quote': "After all, reading is arguably a far more creative and imaginative process than writing; when the reader creates emotion in their head, or the colors of the sky during the setting sun, or the smell of a warm summer's breeze on their face, they should reserve as much praise for themselves as they do for the writer - perhaps more."}]
```

`quote` can also be used as a command line tool:

```sh
>>> max@mbp % quote 'alain de botton'
People only get really interesting when they start to rattle the bars of their cages.

>>> max@mbp % quote --search='alain de botton'
Intimacy is the capacity to be rather weird with someone - and finding that that's ok with them.
```



#### Install

```
pip install -U quote
```



#### Contribute

For feature requests or bug reports, please use [Github Issues](https://github.com/maxhumber/quote/issues)
