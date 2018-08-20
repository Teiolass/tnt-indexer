path = 'data.tnt'

def save_with_duplicates(records):
    txt = ''
    for record in records:
        for key, value in record.items():
            txt += '{}:{}\t'.format(key, value)
        txt += '\n'
    with open(path, 'a') as data:
        data.write(txt)


def get_data():
    with open(path, 'r') as data:
        txt = data.read()
    txt = txt.split('\n')

    res = []
    for line in txt:
        if 'title' not in line:
            continue
        rel = {}
        line = line.split('\t')
        for field in line:
            pt = field.find(':')
            key = field[:pt]
            value = field[pt+1:]
            rel[key] = value
        res.append(rel)
    return res

def save(tosave):
    data = get_data()
    ids = []
    for el in data:
        ids.append(el['torrent'])
    single_tosave = []
    for cand in tosave:
        if cand['torrent'] not in ids:
            single_tosave.append(cand)
    save_with_duplicates(single_tosave)

