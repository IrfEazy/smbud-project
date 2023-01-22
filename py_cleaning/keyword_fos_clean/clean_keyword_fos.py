# Author: Irfan Cela

from json import load, dump
from os import rename, remove
from re import split


def clean(in_file, out_file=None):
    if out_file is None:
        out_file = in_file
    # Opening JSON file
    dataset = open(in_file)
    filtered_file = open('filtered.json', 'w', encoding='utf-8')
    filtered_file.write('[')
    filtered_file.close()

    # returns JSON object as a dictionary
    dblp = load(dataset)

    for node in dblp:
        if 'doi' in node and 'keywords' in node and 'fos' in node and node['doi'] and node['keywords'] and node[
            'fos'] and \
                node['doi'] != 'null':
            last = node

    # Iterating through the json list
    for node in dblp:
        if 'doi' in node and 'keywords' in node and 'fos' in node and node['doi'] and node['keywords'] and node[
            'fos'] and \
                node['doi'] != 'null':
            cleaned_keywords = []
            for keyword in node['keywords']:
                cleaned_string = ''
                for word in split(r'\W+', keyword.lower()):
                    cleaned_string = cleaned_string + word + ' '
                cleaned_keywords.append(cleaned_string.strip())
            node['keywords'] = cleaned_keywords
            cleaned_fos = []
            for fos in node['fos']:
                cleaned_string = ''
                for word in split(r'\W+', fos.lower()):
                    cleaned_string = cleaned_string + word + ' '
                cleaned_fos.append(cleaned_string.strip())
            node['fos'] = cleaned_fos
            if 'isbn' in node and node['isbn']:
                node['publication_type'] = "Book"
            elif 'issn' in node and node['issn']:
                node['publication_type'] = "Journal"
            else:
                node['publication_type'] = "Conference"
            with open('filtered.json', 'a', encoding='utf-8') as filtered_file:
                dump(node, filtered_file, ensure_ascii=False, indent=4)
                if node != last:
                    filtered_file.write(',')

    filtered_file = open('filtered.json', 'a', encoding='utf-8')
    filtered_file.write(']')

    # Closing file
    dataset.close()
    filtered_file.close()
    if in_file == out_file:
        remove(in_file)

    rename('filtered.json', out_file)
