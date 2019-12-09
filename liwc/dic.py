def read_dic(filepath):
    """
    Reads a LIWC lexicon from a file in the .dic format, returning a tuple of
    (lexicon, category_names), where:
    * `lexicon` is a dict mapping string patterns to lists of category names
    * `categories` is a list of category names (as strings)

    """
    # category_mapping is a mapping from integer string to category name
    category_mapping = {}
    # category_names is equivalent to category_mapping.values() but retains original ordering
    category_names = []
    lexicon = {}
    # the mode is incremented by each '%' line in the file
    mode = 0
    for line in open(filepath):
        tsv = line.strip()
        if tsv:
            parts = tsv.split()
            if parts[0] == "%":
                mode += 1
            elif mode == 1:
                # definining categories
                category_names.append(parts[1])
                category_mapping[parts[0]] = parts[1]
            elif mode == 2:
                lexicon[parts[0]] = [
                    category_mapping[category_id] for category_id in parts[1:]
                ]
    return lexicon, category_names
