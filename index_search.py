from collections import defaultdict  # https://docs.python.org/2/library/collections.html

from words import get_text, words


def create_index(files):
    """
    Given a list of fully-qualified filenames, build an index from word
    to set of document IDs. A document ID is just the index into the
    files parameter (indexed from 0) to get the file name. Make sure that
    you are mapping a word to a set of doc IDs, not a list.
    For each word w in file i, add i to the set of document IDs containing w
    Return a dict object mapping a word to a set of doc IDs.
    """
    res_dict = {}
    count = -1
    for file in files:
        count += 1
        if file[-4:] == '.txt':
            word_list = words(get_text(file))
            for word in word_list:
                if word not in res_dict:
                    res_dict[word] = {count}
                else:
                    res_dict[word].add(count)
    return res_dict

def index_search(files, index, terms):
    """
    Given an index and a list of fully-qualified filenames, return a list of
    filenames whose file contents has all words in terms parameter as normalized
    by your words() function.  Parameter terms is a list of strings.
    You can only use the index to find matching files; you cannot open the files
    and look inside.
    """
    res_file =[]
    count = 0
    if len(terms) == 0:
        print('empty terms')
        return
    for term in terms:
        term = term.lower()
        count += 1
        if count == 1:
            try:
                s = index[term]
            except:
                s = set()
        else:
            s = s.intersection(index[term])
    for id in s:
        res_file.append(files[id])
    return res_file

