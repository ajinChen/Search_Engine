import sys
def getdata():
    # if no file given, read from stdin
    if len(sys.argv) == 1:
        data = sys.stdin.read()
    else:
        f = open(sys.argv[1],"r")
        data = f.read()
        f.close()
    return data.strip()

def readcsv(data):
    """
    Read CSV with header from data string and return a header list
    containing a list of names and also return the list of lists
    containing the data.
    """
    res = []
    contains = data.split('\n')
    header = contains.pop(0).split(',')
    for line in contains:
        l = line.split(',')
        res.append(l)
    data = res
    return header, data

