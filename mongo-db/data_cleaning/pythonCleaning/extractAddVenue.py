from json import load, dumps

jsonFile = open('datasetMongo.json', 'r')
values = load(jsonFile)

rawValues = {}
i = 0
for line in values:
    if 'venue' in line:
        rawValues[i] = line['venue']['raw']
        i = i + 1
print(rawValues)

raw = 0
for element in values:
    if 'venue' in element:
        del element['venue']
    if '_id' in element:
        element['venue'] = rawValues[raw]
        raw = raw + 1

with open('addVenue.json', 'w') as jsonF:
    jsonF.write(dumps(values, indent=4))
