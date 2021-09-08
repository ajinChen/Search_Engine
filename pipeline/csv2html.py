import mycsv

def get_html():
    header, data = mycsv.readcsv(mycsv.getdata())
    print('<html>')
    print('<body>')
    print('<table>')
    hl = '<tr>'
    for h in header:
        hl += '<th>' + h + '</th>'
    hl += '</tr>'
    print(hl)
    for line in data:
        dl = '<tr>'
        for elem in line:
            dl += '<td>' + elem + '</td>'
        dl += '</tr>'
        print(dl)
    print('</table>')
    print('</body>')
    print('</html>')


# interactive section
get_html()