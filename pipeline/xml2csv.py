import mycsv
import xmltodict

def readxml(data):
    xml = xmltodict.parse(data)
    header = xml['file']['headers'].split(',')
    d = []
    for line in xml['file']['data']['record']:
        res = []
        for tag in header:
            if ' ' in tag:
                tag = tag.replace(' ', '_')
            res.append(line[tag])
        d.append(res)
    data = d
    return header, data

def get_xml2csv():
    header, data = readxml(mycsv.getdata())
    print(','.join(header))
    for row in data:
        print(','.join(row).strip('/n').strip())


# interactive section
get_xml2csv()