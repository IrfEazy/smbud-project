from sys import argv

from keyword_fos_clean.clean_keyword_fos import clean
from keyword_fos_clean.extractAddVenue import extract_and_rewrite
from location import location_adder
from publisher import publisher_adder
from references import add_references
from regx import rm_incorrect_issn
from section_adder.author import email_bio_date_adder
from section_adder.section_adder import add_sections
from type import type_adder


def clean():
    if argv is not None and len(argv) > 1:
        if argv[1] is not None:
            in_file = out_file = argv[1]
        if argv[2] is not None:
            out_file = argv[2]
    else:
        print("Too few arguments. I want at least an input file")
        return

    print("First phase cleaning started...")
    rm_incorrect_issn(in_file, out_file)
    print("Incorrect ISSN removed")
    clean(out_file, out_file)
    print("Keyword cleaning done")
    # keywords.fos_keywords_adder(out_file, out_file)
    # print("Keyword added")
    add_references(out_file, out_file)
    print("References created")
    type_adder(out_file, out_file)
    print("Type added")
    publisher_adder(out_file, out_file)
    print("Publishers added")
    location_adder(out_file, out_file)
    print("Location added")
    extract_and_rewrite(out_file, out_file)
    print("Venue extracted and rewritten")

    print("Adding sections and authors (MongoDB part)")
    add_sections(out_file, out_file)
    print("Sections added")
    email_bio_date_adder(out_file, out_file)
    print("Authors added")


if __name__ == '__main__':
    clean()
