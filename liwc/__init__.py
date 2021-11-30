from .dic import read_dic
from .trie import build_trie, search_trie

try:
    import pkg_resources

    __version__ = pkg_resources.get_distribution("liwc").version
except Exception:
    __version__ = None


def load_token_parser(filepath, encoding = "utf-8"):
    """
    Reads a LIWC lexicon from a file in the .dic format, returning a tuple of
    (parse, category_names), where:
    * `parse` is a function from a token to a list of strings (potentially
      empty) of matching categories
    * `category_names` is a list of strings representing all LIWC categories in
      the lexicon
    `encoding = "utf-8"` can be overwritten by other encoding such as "EUC-JP" for Janpanese "IOS-2022" for
    Simplified Chinese. The second default is "windows-1252" when the load_token_parser encounters non utf-8
    encoding.
    """
    lexicon, category_names = read_dic(filepath, encoding = encoding)
    trie = build_trie(lexicon)

    def parse_token(token):
        for category_name in search_trie(trie, token):
            yield category_name

    return parse_token, category_names
