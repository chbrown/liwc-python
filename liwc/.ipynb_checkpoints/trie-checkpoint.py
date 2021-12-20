def build_trie(lexicon):
    """
    Build a character-trie from the plain pattern_string -> categories_list
    mapping provided by `lexicon`.

    Some LIWC patterns end with a `*` to indicate a wildcard match.
    """
    trie = {}
    for pattern, category_names in lexicon.items():
        cursor = trie
        for char in pattern:
            if char == "*":
                cursor["*"] = category_names
                break
            if char not in cursor:
                cursor[char] = {}
            cursor = cursor[char]
        cursor["$"] = category_names
    return trie


def search_trie(trie, token, token_i=0):
    """
    Search the given character-trie for paths that match the `token` string.
    """
    if "*" in trie:
        return trie["*"]
    if "$" in trie and token_i == len(token):
        return trie["$"]
    if token_i < len(token):
        char = token[token_i]
        if char in trie:
            return search_trie(trie[char], token, token_i + 1)
    return []
