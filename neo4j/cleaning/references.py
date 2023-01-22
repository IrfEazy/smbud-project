# Sample array of references
from json import load, dumps

from numpy import random

max_ref_count = 10


def add_references(in_file, out_file):
    references = []

    # Open JSON file
    f = open(in_file)
    f2 = out_file

    # Return json object as a dictionary
    data = load(f)

    for i in data:
        if '_id' in i:
            references.append(i['_id'])

    for i in data:
        if 'references' not in i and random.randint(0, 15) != 0:
            refs = list(set(list(random.choice(references, random.randint(0, max_ref_count)))))
            if i['_id'] in refs:
                refs.remove(i['_id'])

            i['references'] = refs

    with open(f2, 'w') as out:
        out.write(dumps(data, indent=4))
