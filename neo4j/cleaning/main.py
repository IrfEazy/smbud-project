from sys import argv

from keywords import fos_keywords_adder
from location import location_adder
from publisher import publisher_adder
from references import add_references
from regx import rm_incorrect_issn
from type import type_adder


def clean():
    in_file = 'data/orig_prova.json'
    out_file = 'data/out.json'

    if argv is not None and len(argv) > 1:
        if argv[1] is not None:
            in_file = argv[1]
        if argv[2] is not None:
            out_file = argv[2]

    rm_incorrect_issn(in_file, out_file)
    fos_keywords_adder(out_file, out_file)
    add_references(out_file, out_file)
    type_adder(out_file, out_file)
    publisher_adder(out_file, out_file)
    location_adder(out_file, out_file)

    # f = open('data/orig_prova.json')
    # with open('data/out_re.json', 'w') as out:
    #     for line in f.readlines():
    #         line = re.sub(r'"issn" : "[A-Za-z].*"', r'"issn" : ""', line)


if __name__ == '__main__':
    clean()
