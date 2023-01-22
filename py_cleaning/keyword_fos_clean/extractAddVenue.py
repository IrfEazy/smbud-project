# Author: Bianca Christian Savoiu Marinas

from json import load, dumps


def extract_and_rewrite(in_file, out_file=None):
    if out_file is None:
        out_file = in_file

    json_file = open(in_file, 'r')
    values = load(json_file)

    raw_values = {}
    i = 0
    for line in values:
        if 'venue' in line:
            raw_values[i] = line['venue']['raw']
            i = i + 1

    raw = 0
    for element in values:
        if 'venue' in element:
            del element['venue']
        if '_id' in element:
            element['venue'] = raw_values[raw]
            raw = raw + 1

    with open(out_file, 'w') as jsonF:
        jsonF.write(dumps(values, indent=4))
