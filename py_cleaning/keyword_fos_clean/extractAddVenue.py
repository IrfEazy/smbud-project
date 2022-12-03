# Author: Bianca Christian Savoiu Marinas

import json


def extract_and_rewrite(in_file, out_file=None):
    if out_file is None:
        out_file = in_file

    jsonFile = open(in_file, 'r')
    values = json.load(jsonFile)

    rawValues = {}
    i = 0
    for line in values:
        if 'venue' in line:
            rawValues[i] = line['venue']['raw']
            i = i + 1

    raw = 0
    for element in values:
        if 'venue' in element:
            del element['venue']
        if '_id' in element:
            element['venue'] = rawValues[raw]
            raw = raw + 1

    with open(out_file, 'w') as jsonF:
        jsonF.write(json.dumps(values, indent=4))
