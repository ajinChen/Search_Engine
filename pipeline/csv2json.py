import mycsv

def get_json():
    header, data = mycsv.readcsv(mycsv.getdata())
    print('{')
    hl = ' ' * 2 + '"headers":['
    for h in header:
        hl += '"' + h + '"' + ','
    hl = hl.strip(',')
    hl += '],'
    print(hl)
    print(' ' * 2 + '"data":[')
    for index1, line in enumerate(data):
        print(' ' * 4 + '{')
        dl = ' ' * 6
        for index2, elem in enumerate(line):
            tag = header[index2]
            if index2 < len(line) - 1:
                dl += '"' + tag + '":' + '"' + elem + '"' + ', '
            else:
                dl += '"' + tag + '":' + '"' + elem + '"'
        print(dl)
        if index1 < len(data)-1:
            print(' ' * 4 + '},')
        else:
            print(' ' * 4 + '}')
    print(' ' * 2 + ']')
    print('}')


# interactive section
get_json()
