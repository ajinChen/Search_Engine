# Got slate magazine data from http://www.anc.org/data/oanc/contents/
# rm'd .xml, .anc files, leaving just .txt
# 4534 files in like 55 subdirs
import htable
from htable import *
from words import get_text, words


def myhtable_create_index(files):
    """
    Build an index from word to set of document indexes
    This does the exact same thing as create_index() except that it uses
    your htable.  As a number of htable buckets, use 4011.
    Returns a list-of-buckets hashtable representation.
    """
    res_buckets = htable(4011)
    for id, file in enumerate(files):
        if file[-4:] == '.txt':
            word_list = words(get_text(file))
            for word in word_list:
                value = htable_get(res_buckets, word)
                if value == None:
                    htable_put(res_buckets, word, {id})
                else:
                    value.add(id)
                    htable_put(res_buckets, word, value)
    return res_buckets


def myhtable_index_search(files, index, terms):
    """
    This does the exact same thing as index_search() except that it uses your htable.
    I.e., use htable_get(index, w) not index[w].
    """
    res_file = []
    count = 0
    if len(terms) == 0:
        print('empty terms')
        return
    for term in terms:
        term = term.lower()
        count += 1
        if count == 1:
            s = htable_get(index, term)
            if s == None:
                s = {-1}
        else:
            s = s.intersection(htable_get(index, term))
    for id in s:
        if id != -1:
            res_file.append(files[id])
    return res_file