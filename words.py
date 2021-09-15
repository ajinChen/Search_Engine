import os
import re
import string


def filelist(pwd):
    """Return a fully-qualified list of filenames under root directory"""
    fully_qualified_list = []
    for root, dirs, files in sorted(os.walk(pwd)):
        for filename in files:
            filepath = os.path.join(root, filename)
            fully_qualified_list.append(filepath)
    return fully_qualified_list

def get_text(fileName):
    f = open(fileName, encoding='latin-1')
    s = f.read()
    f.close()
    return s


def words(text):
    """
    Given a string, return a list of words normalized as follows.
    Split the string to make words first by using regex compile() function
    and string.punctuation + '0-9\\r\\t\\n]' to replace all those
    char with a space character.
    Split on space to get word list.
    Ignore words < 3 char long.
    Lowercase all words
    """
    regex = re.compile('[' + re.escape(string.punctuation) + '0-9\\r\\t\\n]')
    nopunct = regex.sub(" ", text)  # delete stuff but leave at least a space to avoid clumping together
    words = nopunct.split(" ")
    words = [w for w in words if len(w) > 2]  # ignore a, an, to, at, be, ...
    words = [w.lower() for w in words]
    # print words
    return words


def results(docs, terms):
    """
    Given a list of fully-qualifed filenames, return an HTML file
    that displays the results and up to 2 lines from the file
    that have at least one of the search terms.
    Return at most 100 results.  Arg terms is a list of string terms.
    """
    html = ''
    html += '<html>\n'
    html += ' ' * 4 + '<body>\n'
    html += ' ' * 4 + '<h2>Search results for <b>'
    count = 0
    for term in terms:
        count += 1
        html += term
        if count < len(terms):
            html += ' '
    html += '</b> in ' + str(len(docs)) + ' files</h2>\n'
    html += '\n'
    count = 0
    for filename in docs:
        count += 1
        if count < 101:
            html += ' ' * 8 + '<p><a href="file://' + filename + '">' + filename + '</a><br>\n'
            # find one line terms
            with open(filename, mode='r') as f:
                html += ' ' * 8
                for line in f.readlines():
                    line = line.lower()
                    flag = 0
                    for term in terms:
                        term = term.lower()
                        if term in words(line):
                            line = line.replace(term, '<b>' + term + '</b>')
                            flag += 1
                    if flag > 0:
                        html += line.strip('\n') + '<br><br>\n\n'
                        break
    html += '</body>\n'
    html += '</html>'
    return html


def filenames(docs):
    """Return just the filenames from list of fully-qualified filenames"""
    if docs is None:
        return []
    return [os.path.basename(d) for d in docs]

"""
docs = ['/Users/ajin/data/slate/51/ArticleIP_38825.txt']
terms = ['ronald', 'reagan']
print(results(docs, terms))
"""