# `liwc`

[![PyPI version](https://badge.fury.io/py/liwc.svg)](https://pypi.org/project/liwc/)
[![Travis CI Build Status](https://travis-ci.org/chbrown/liwc-python.svg?branch=master)](https://travis-ci.org/chbrown/liwc-python)

This repository is a Python package implementing two basic functions:
1. Loading (parsing) a Linguistic Inquiry and Word Count (LIWC) dictionary from the `.dic` file format.
2. Using that dictionary to count category matches on provided texts.

This is not an official LIWC product nor is it in any way affiliated with the LIWC development team or Receptiviti.


## Obtaining LIWC

The LIWC lexicon is proprietary, so it is _not_ included in this repository.

The lexicon data can be acquired (purchased) from [liwc.net](http://liwc.net/).


## Setup

Install from [PyPI](https://pypi.python.org/pypi/liwc):

    pip install liwc


## Example

This example reads the LIWC dictionary from a file named `LIWC2007_English100131.dic`, which looks like this:

    %
    1   funct
    2   pronoun
    [...]
    %
    a   1   10
    abdomen*    146 147
    about   1   16  17
    [...]


#### Loading the lexicon

```python
import liwc
parse, category_names = liwc.load_token_parser('LIWC2007_English100131.dic')
```

* `parse` is a function from a token of text (a string) to a list of matching LIWC categories (a list of strings)
* `category_names` is all LIWC categories in the lexicon (a list of strings)


#### Analyzing text

```python
import re

def tokenize(text):
    # you may want to use a smarter tokenizer
    for match in re.finditer(r'\w+', text, re.UNICODE):
        yield match.group(0)

gettysburg = '''Four score and seven years ago our fathers brought forth on
  this continent a new nation, conceived in liberty, and dedicated to the
  proposition that all men are created equal. Now we are engaged in a great
  civil war, testing whether that nation, or any nation so conceived and so
  dedicated, can long endure. We are met on a great battlefield of that war.
  We have come to dedicate a portion of that field, as a final resting place
  for those who here gave their lives that that nation might live. It is
  altogether fitting and proper that we should do this.'''.lower()
gettysburg_tokens = tokenize(gettysburg)
```

Now, count all the categories in all of the tokens, and print the results:

```python
from collections import Counter
gettysburg_counts = Counter(category for token in gettysburg_tokens for category in parse(token))
print(gettysburg_counts)
#=> Counter({'funct': 58, 'pronoun': 18, 'cogmech': 17, ...})
```

### _N.B._:

* The LIWC lexicon only matches lowercase strings, so you will most likely want to lowercase your input text before passing it to `parse(...)`.
  In the example above, I call `.lower()` on the entire string, but you could alternatively incorporate that into your tokenization process (e.g., by using [spaCy](https://spacy.io/api/token)'s `token.lower_`).


## License

Copyright (c) 2012-2020 Christopher Brown.
[MIT Licensed](LICENSE.txt).
