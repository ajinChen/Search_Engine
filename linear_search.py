# Got slate magazine data from http://www.anc.org/data/oanc/contents/
# rm'd .xml, .anc files, leaving just .txt
# 4534 files in like 55 subdirs

from words import get_text, words


def linear_search(files, terms):
    """
    Given a list of fully-qualified filenames, return a list of them
    whose file contents has all words in terms as normalized by your words() function.
    Parameter terms is a list of strings.
    Perform a linear search, looking at each file one after the other.
    """
    res = []
    for file in files:
        if file[-4:] == '.txt':
            word_list = words(get_text(file))
            flag = 0
            for term in terms:
                term = term.lower()
                if term in word_list:
                    flag += 1
            if flag == len(terms):
                res.append(file)
    return res