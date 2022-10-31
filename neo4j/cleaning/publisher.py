import json
import numpy as np


#requires that the type of publication is already assigned to each paper
#add the field publisher to all paper whose publication_type is Bool or Journal
def publisher_adder(in_file, out_file):
    with open(in_file) as f:
        data = json.load(f)

    with open('data/publishers.json') as pub:
        pubs = json.load(pub)

    publishers = []

    for i in range(len(pubs)):
        publishers.append(pubs[i]["publisher"])
    
    for i in range(len(data)):
        if data[i]["publication_type"] == "Book" or data[i]["publication_type"] == "Journal":
            data[i]["publisher"] = publishers[np.random.randint(0, len(publishers))]
    
    with open(out_file, 'w') as f:
        json.dump(data, f, indent=4)