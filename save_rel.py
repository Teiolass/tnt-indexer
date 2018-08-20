path = 'data.tnt'

def save_with_duplicates(records):
    txt = ''
    for record in records:
        for key, value in record.items():
            txt += '{}:{} '.format(key, value)
        txt += '\n'
    with open(path, a) as data:
        data.append(txt)


def get_data():
    with open(path, 'r') as data:
        txt = data.read()
    txt = txt.split('\n')

    res = []
    for line in txt:
        rel = {}
        line = line.split(' ')
        for field in line:
            pt = field.find(':')
            key = field[:pt]
            value = field[pt+1:]
            rel[key] = value
        res.append(rel)
    return res

                
