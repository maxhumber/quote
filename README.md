<h3 align="center">
  <img src="https://raw.githubusercontent.com/maxhumber/quote/master/quote.png" height="300px" alt="quote">
</h3>
<p align="center">
  <a href="https://opensource.org/licenses/MIT"><img alt="MIT" src="https://img.shields.io/github/license/maxhumber/quote.svg"></a>
  <a href="https://travis-ci.org/maxhumber/quote"><img alt="Travis" src="https://img.shields.io/travis/maxhumber/quote.svg"></a>
  <a href="https://pypi.python.org/pypi/quote"><img alt="PyPI" src="https://img.shields.io/pypi/v/quote.svg"></a>
  <a href="https://pypi.python.org/pypi/quote"><img alt="Downloads" src="https://img.shields.io/pypi/dm/quote.svg"></a>
</p>



#### About

quote is a python wrapper for the Goodreads Quote API, powered by [gazpacho](https://github.com/maxhumber/gazpacho).

#### Usage

quote is simple to use:

```python
import json
from quote import search

query = 'blake crouch'
result = search(query, limit=2)
json.loads(result)

# [{'author': 'Blake Crouch',
#   'book': 'Dark Matter',
#   'quote': "We're more than the sum total of our choices, that all the paths we might have taken factor somehow into the math of our identity."},
#  {'author': 'Blake Crouch',
#   'book': 'Dark Matter',
#   'quote': 'No one tells you it’s all about to change, to be taken away. There’s no proximity alert, no indication that you’re standing on the precipice. And maybe that’s what makes tragedy so tragic. Not just what happens, but how it happens: a sucker punch that comes at you out of nowhere, when you’re least expecting it. No time to flinch or brace.'}]

```



#### Installation

```
pip install quote
```



#### Contribute

For feature requests or bug reports, please use [Github Issues](https://github.com/maxhumber/quote/issues)