from json import load, dump

from numpy import random


# requires that the type of publication is already assigned to each paper
# add the field publisher to all paper whose publication_type is Bool or Journal
def publisher_adder(in_file, out_file):
    with open(in_file) as f:
        data = load(f)

    with open('data/publishers.json') as pub:
        pubs = load(pub)

    publishers = []

    for i in range(len(pubs)):
        publishers.append(pubs[i]["publisher"])

    for i in range(len(data)):
        if data[i]["publication_type"] == "Book" or data[i]["publication_type"] == "Journal":
            if 'publisher' in data[i] and data[i]["publisher"] is not None and data[i]["publisher"] != "":
                continue
            data[i]["publisher"] = publishers[random.randint(0, len(publishers))]

    with open(out_file, 'w') as f:
        dump(data, f, indent=4)
