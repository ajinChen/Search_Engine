"""
A hashtable represented as a list of lists with open hashing.
Each bucket is a list of (key,value) tuples
"""

def htable(nbuckets):
    """Return a list of nbuckets lists"""
    return [[] for i in range(nbuckets)]


def hashcode(o):
    """
    Return a hashcode for strings and integers; all others return None
    For integers, just return the integer value.
    For strings, perform operation h = h*31 + ord(c) for all characters in the string
    """
    # may be some problem with search integer number
    if isinstance(o, int):
        return o
    elif isinstance(o, str):
        h = 0
        for c in o:
            h = h * 31 + ord(c)
        return h
    else:
        return None


def bucket_indexof(table, key):
    """
    You don't have to implement this, but I found it to be a handy function.
    Return the index of the element within a specific bucket; the bucket is:
    table[hashcode(key) % len(table)]. You have to linearly
    search the bucket to find the tuple containing key.
    """
    for index, tp in enumerate(table[hashcode(key) % len(table)]):
        if key == tp[0]:
            return index
    return -1


def htable_put(table, key, value):
    """
    Perform the equivalent of table[key] = value
    Find the appropriate bucket indicated by key and then append (key,value)
    to that bucket if the (key,value) pair doesn't exist yet in that bucket.
    If the bucket for key already has a (key,value) pair with that key,
    then replace the tuple with the new (key,value).
    Make sure that you are only adding (key,value) associations to the buckets.
    The type(value) can be anything. Could be a set, list, number, string, anything!
    """
    n_buck = hashcode(key) % len(table)
    if len(table[n_buck]) == 0:
        target = (key, value)
        table[n_buck].append(target)
    else:
        for idx, elem in enumerate(table[n_buck]):
            if key == elem[0]:
                table[n_buck].pop(idx)
        target = (key, value)
        table[n_buck].append(target)
    return


def htable_get(table, key):
    """
    Return the equivalent of table[key].
    Find the appropriate bucket indicated by the key and look for the
    association with the key. Return the value (not the key and not
    the association!). Return None if key not found.
    """
    n_buck = hashcode(key) % len(table)
    for elem in table[n_buck]:
        if key == elem[0]:
            return elem[1]
    return None


def htable_buckets_str(table):
    """
    Return a string representing the various buckets of this table.
    The output looks like:
        0000->
        0001->
        0002->
        0003->parrt:99
        0004->
    where parrt:99 indicates an association of (parrt,99) in bucket 3.
    """
    output = ''
    n_bucket = -1
    for bucket in table:
        n_bucket += 1
        output += str(n_bucket).rjust(4, '0') + '->'
        # be caeful for different format / list
        for elem in bucket:
            output += str(elem[0]) + ':' + str(elem[1]) + ', '
        output = output.strip(' ').strip(',')
        output += '\n'
    return output


def htable_str(table):
    """
    Return what str(table) would return for a regular Python dict
    such as {parrt:99}. The order should be in bucket order and then
    insertion order within each bucket. The insertion order is
    guaranteed when you append to the buckets in htable_put().
    """
    s = '{'
    for bucket in table:
        for tup in bucket:
            s += str(tup[0]) + ':'
            s += str(tup[1]) + ', '
    s = s.strip().strip(',')
    s += '}'
    return s