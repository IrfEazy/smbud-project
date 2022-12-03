import json

import numpy as np

lim = 1000  # max numero di keywords
max_kwords_paper = 10  # max number of keywords per paper

# filename = sys.argv[1]
filename = 'data/orig_prova.json'


def fos_keywords_adder(in_file, out_file):
    with open(in_file) as f:
        data = json.load(f)

    fos_kw_map = {}

    # creating a mapping of keywords to field of study
    for j_obj in data:
        if 'fos' in j_obj and 'keywords' in j_obj:
            keywords = j_obj['keywords']

            # discarding leading and trailing spaces
            keywords = list(map(lambda x: x.strip(), keywords))
            keys = j_obj['fos']
            for key in keys:
                if key in fos_kw_map:
                    # avoiding duplicates
                    for kword in keywords:
                        if kword not in fos_kw_map[key]:
                            fos_kw_map[key].append(kword)
                else:
                    # removing duplicates in their in the list
                    fos_kw_map[key] = list(dict.fromkeys(keywords))

    with open('data/fos-keywords.json', 'w') as kmap:
        json.dump(fos_kw_map, kmap, indent=4)

    # ADDING FOS AND KEYWORDS
    for j_obj in data:
        if 'fos' in j_obj:
            foss = j_obj['fos']  # a list
            if 'keywords' not in j_obj or j_obj['keywords'] == []:
                j_obj['keywords'] = extract_rand_keywords(fos_kw_map, foss)
        else:
            # assign random fos
            j_obj['fos'] = foss = \
                list(
                    # remove duplicates
                    dict.fromkeys(
                        # take random keys
                        np.random.choice(
                            list(fos_kw_map.keys()), np.random.randint(1, max_kwords_paper)
                        )
                    )
                )
            # assigning keywords
            if 'keywords' not in j_obj:
                j_obj['keywords'] = extract_rand_keywords(fos_kw_map, foss)
            else:
                j_obj['keywords'] += extract_rand_keywords(fos_kw_map, foss)

    with open(out_file, 'w') as f:
        json.dump(data, f, indent=4)


def extract_rand_keywords(fos_kw_map, foss):
    candidates = []
    for fos in foss:
        candidates += [kword for kword in fos_kw_map[fos] if kword not in candidates]

    if len(candidates) > 1:
        # print(candidates, max_kwords_paper, len(candidates))
        candidates = np.random.choice(candidates, np.random.randint(1, min(max_kwords_paper, len(candidates))))
        # remove duplicates
        return list(dict.fromkeys(candidates))
    else:
        return []

# type.typeAdder(filename)
# modifyJSONmain.addReferences(filename, filename)
#
# print("done ")
