import json
import re

# Opening JSON file
dataset = open('data/test.json')
filteredFile = open('filtered.json', 'w', encoding='utf-8')
filteredFile.write('[')
filteredFile.close()

# returns JSON object as a dictionary
dblp = json.load(dataset)

for node in dblp:
    if 'doi' in node and 'keywords' in node and 'fos' in node and node['doi'] and node['keywords'] and node['fos'] and \
            node['doi'] != 'null':
        last = node

# Iterating through the json list
for node in dblp:
    if 'doi' in node and 'keywords' in node and 'fos' in node and node['doi'] and node['keywords'] and node['fos'] and \
            node['doi'] != 'null':
        cleanedKeywords = []
        for keyword in node['keywords']:
            cleanedString = ''
            for word in re.split(r'\W+', keyword.lower()):
                cleanedString = cleanedString + word + ' '
            cleanedKeywords.append(cleanedString.strip())
        node['keywords'] = cleanedKeywords
        cleanedFos = []
        for fos in node['fos']:
            cleanedString = ''
            for word in re.split(r'\W+', fos.lower()):
                cleanedString = cleanedString + word + ' '
            cleanedFos.append(cleanedString.strip())
        node['fos'] = cleanedFos
        if 'isbn' in node and node['isbn']:
            node['publication_type'] = "Book"
        elif 'issn' in node and node['issn']:
            node['publication_type'] = "Journal"
        else:
            node['publication_type'] = "Conference"
        with open('filtered.json', 'a', encoding='utf-8') as filteredFile:
            json.dump(node, filteredFile, ensure_ascii=False, indent=4)
            if node != last:
                filteredFile.write(',')

filteredFile = open('filtered.json', 'a', encoding='utf-8')
filteredFile.write(']')

# Closing file
dataset.close()
filteredFile.close()
