#!/usr/bin/env python3
from urllib import request, parse


url = 'http://www.tntvillage.scambioetico.org/src/releaselist.php'

data_dic = {
        'page': 4
}

data = parse.urlencode(data_dic).encode()
req =  request.Request(url, data=data)
resp = request.urlopen(req)
txt = resp.read().decode('utf-8')

begin = txt.find('Titolo') + 18
end = txt.find('</table>')
txt = txt[begin:end]

txt = txt.replace('&#39;', '\'')

lines = txt.split('\n')
for line in lines:
    if 'magnet' not in line:
        lines.remove(line)

for line in lines:
    rel = {}
    start = line.find('href') + 6
    end = line[start:].find('\'') + start
    rel['torrent'] = line[start:end]
    line = line[end:]

    start = line.find('href') + 6
    end = line[start:].find('\'') + start
    rel['magnet'] = line[start:end]
    line = line[end:]
  
    start = line.find('cat=') + 4 
    end = line[start:].find('\'') + start
    rel['category'] = line[start:end]
    line = line[end:]

    start = line.find('href') + 6
    end = line[start:].find('\'') + start
    rel['link'] = line[start:end]
    line = line[end:]

    start = line.find('>') + 1
    end = line[start:].find('<') + start
    rel['title'] = line[start:end]
    line = line[end:]
    
    start = line.find('>') + 7
    end = line[start:].find('<') + start
    rel['description'] = line[start:end]
    line = line[end:]

    for key, value in rel.items():
        print('{}: {}'.format(key,  value))

    print('\n\n')

