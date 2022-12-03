# Sample array of references
import json

import numpy as np

max_ref_count = 10


def addReferences(in_file, out_file):
    references = []

    # Open JSON file
    f = open(in_file)
    f2 = out_file

    # Return json object as a dictionary
    data = json.load(f)

    for i in data:
        if '_id' in i:
            references.append(i['_id'])

    for i in data:
        if 'references' not in i and np.random.randint(0, 15) != 0:
            refs = list(set(list(np.random.choice(references, np.random.randint(0, max_ref_count)))))
            if i['_id'] in refs:
                refs.remove(i['_id'])

            i['references'] = refs

    with open(f2, 'w') as out:
        out.write(json.dumps(data, indent=4))
