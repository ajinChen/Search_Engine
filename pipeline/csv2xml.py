import mycsv

def get_xml():
    header, data = mycsv.readcsv(mycsv.getdata())
    print('<?xml version="1.0"?>')
    print('<file>')
    hl = ' ' * 2 + '<headers>'
    for h in header:
        hl += h + ','
    hl = hl.strip(',')
    hl += '</headers>'
    print(hl)
    print(' ' * 2 + '<data>')
    for line in data:
        print(' ' * 4 + '<record>')
        dl = ' ' * 6
        for index, elem in enumerate(line):
            if ' ' in header[index]:
                tag = header[index].replace(' ', '_')
            else:
                tag = header[index]
            dl += '<' + tag + '>' + elem + '</' + tag + '>'
        print(dl)
        print(' ' * 4 + '</record>')
    print(' ' * 2 + '</data>')
    print('</file>')


# interactive section
get_xml()