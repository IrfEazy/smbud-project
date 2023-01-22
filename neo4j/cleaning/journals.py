from json import dump
from re import split
from xml.etree.ElementTree import parse


def add_publishers(in_file, out_file):
    # Open XML
    f = open(in_file)

    # Return json object as a dictionary
    data = parse(f)
    jdata = []
    root = data.getroot()

    for tr in root.iter('tr'):
        i = 0
        dic = {}
        for td in tr.iter('td'):
            if i == 0:
                dic['index'] = td.text
            elif i == 1:
                for a in td.iter('a'):
                    dic['journal'] = a.text
            elif i == 2:
                issns = split(',', td.text)
                issns = list(map(lambda x: x.strip(), issns))
                dic['issn'] = issns
            elif i == 3:
                dic['publisher'] = td.text
            i += 1

        jdata.append(dic)

    with open(out_file, 'w') as f:
        dump(jdata, f, indent=4)


add_publishers('data/jls.txt', 'data/publishers.json')
