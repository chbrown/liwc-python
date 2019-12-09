import os.path

import liwc

test_dir = os.path.dirname(__file__)


def test_category_names():
    _, category_names = liwc.load_token_parser(os.path.join(test_dir, "alpha.dic"))
    assert category_names == ["A", "Bravo"]


def test_parse():
    parse, _ = liwc.load_token_parser(os.path.join(test_dir, "alpha.dic"))
    sentence = "Any alpha a bravo charlie Bravo boy"
    tokens = sentence.split()
    matches = [category for token in tokens for category in parse(token)]
    # matching is case-sensitive, so the only matches are "alpha" (A), "a" (A) and "bravo" (Bravo)
    assert matches == ["A", "A", "Bravo"]
