import sys

import keywords
import location
import publisher
import references
import regx
import type


def clean():
    in_file = 'data/orig_prova.json'
    out_file = 'data/out.json'

    if sys.argv is not None and len(sys.argv) > 1:
        if sys.argv[1] is not None:
            in_file = sys.argv[1]
        if sys.argv[2] is not None:
            out_file = sys.argv[2]

    regx.rm_incorrect_issn(in_file, out_file)
    keywords.fos_keywords_adder(out_file, out_file)
    references.addReferences(out_file, out_file)
    type.typeAdder(out_file, out_file)
    publisher.publisher_adder(out_file, out_file)
    location.location_adder(out_file, out_file)

    # f = open('data/orig_prova.json')
    # with open('data/out_re.json', 'w') as out:
    #     for line in f.readlines():
    #         line = re.sub(r'"issn" : "[A-Za-z].*"', r'"issn" : ""', line)


if __name__ == '__main__':
    clean()
