import keywords
import references
import sys
import type
import publisher
import location
import regx
import keyword_fos_clean.clean_keyword_fos as clean_keyword_fos
import section_adder.section_adder as section_adder
import section_adder.author as author


def clean():

    if sys.argv is not None and len(sys.argv) > 1:
        if sys.argv[1] is not None:
            in_file = out_file = sys.argv[1]
        if sys.argv[2] is not None:
            out_file = sys.argv[2]
    else:
        print("Too few arguments. I want at least an input file")
        return

    print("First phase cleaning started...")
    regx.rm_incorrect_issn(in_file, out_file)
    print("Incorrect ISSN removed")
    clean_keyword_fos.clean(out_file, out_file)
    print("Keyword cleaning done")
    keywords.fos_keywords_adder(out_file, out_file)
    print("Keyword added")
    references.addReferences(out_file, out_file)
    print("References created")
    type.typeAdder(out_file, out_file)
    print("Type added")
    publisher.publisher_adder(out_file, out_file)
    print("Publishers added")
    location.location_adder(out_file, out_file)
    print("Location added")

    print("Adding sections and authors (MongoDB part)")
    section_adder.add_sections(out_file, out_file)
    print("Sections added")
    author.email_bio_date_adder(out_file, out_file)
    print("Authors added")


if __name__ == '__main__':
    clean()

