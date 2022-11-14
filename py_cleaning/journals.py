import xml.etree.ElementTree as ET
import re, json

def addPublishers(in_file, out_file):
    references = []

    # Open XML
    f = open(in_file)

    # Return json object as a dictionary
    data = ET.parse(f)
    jdata = []
    root = data.getroot()

    for tr in root.iter('tr'):
        i = 0
        dic = {}
        for td in tr.iter('td'):
            if i == 0:
                dic['index'] = td.text
            elif i ==1:
                for a in td.iter('a'):
                    dic['journal'] = a.text
            elif i == 2:
                issns = re.split(',', td.text)
                issns = list(map(lambda x: x.strip(), issns))
                dic['issn'] = issns
            elif i == 3:
                dic['publisher'] = td.text
            i += 1

        jdata.append(dic)

    with open(out_file, 'w') as f:
        json.dump(jdata, f, indent=4)


addPublishers('data/jls.txt', 'data/publishers.json')
