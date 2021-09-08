import mycsv
import json

def readjson(data):
    data = json.loads(data)
    header = data['headers']
    d = []
    for line in data['data']:
        res = []
        for tag in header:
            res.append(line[tag])
        d.append(res)
    data = d
    return header, data

def get_json2csv():
    header, data = readjson(mycsv.getdata())
    print(','.join(header))
    for row in data:
        print(','.join(row).strip('/n').strip())

# interactive section
get_json2csv()