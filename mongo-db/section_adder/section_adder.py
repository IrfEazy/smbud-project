import csv
import json
import os.path
import sys

import numpy as np

import author

# Starting from depth 0
BASE_DEPTH = 0
MAX_SECTION_DEPTH = 1
MAX_SUBSECTION = 5
MAX_SECTIONS = 10

MAX_PAR = 5

REVIEWS_FILE = 'data/Reviews.csv'
SECTIONS_FILE = 'data/sections.json'
URL_FILE = 'data/random_image_URLs.json'
CAPTION_FILE = 'data/random_captions.json'

RAND_PAR = np.random.RandomState(672584343)
RAND_SECTION_DEPTH = np.random.RandomState(267524343)
RAND_SUBSECTIONS = np.random.RandomState(456742563)
RAND_SECTIONS = np.random.RandomState(344198764)


def add_sections(in_file, out_file=None):
    if out_file is None:
        out_file = in_file

    if not os.path.exists(SECTIONS_FILE):
        create_sections()

    with open(SECTIONS_FILE) as sec_f:
        sections_data = json.load(sec_f)

    with open(in_file) as i_file:
        paper_dataset = json.load(i_file)

    # Integer division
    max_sections = MAX_SECTIONS
    min_sections = max_sections // 2
    if min_sections < 1:
        raise Exception("Too few sections")

    for paper in paper_dataset:
        indx = RAND_SECTIONS.randint(0, len(sections_data))
        sections = [sections_data[indx] for i in range(RAND_SECTIONS.randint(min_sections, max_sections))]
        paper['sections'] = sections

    with open(out_file, 'w') as ofile:
        json.dump(paper_dataset, ofile, indent=4)


def create_sections():
    json_out = []
    with open(REVIEWS_FILE) as f:
        csv_data = csv.DictReader(f)
        csv_data_iter = csv_data.__iter__()

        with open(URL_FILE) as url_f:
            url_data = json.load(url_f)

        with open(CAPTION_FILE) as caption_f:
            caption_data = json.load(caption_f)

            try:
                while True:
                    depth_level = 1
                    json_out.append(create_section(csv_data_iter, url_data, caption_data, BASE_DEPTH, depth_level))
            except StopIteration:
                print("Sections created!")

    with open(SECTIONS_FILE, 'w') as ofile:
        json.dump(json_out, ofile, indent=4)


def create_section(csv_iterator, urls, captions, level, max_depth):
    try:
        if level > max_depth:
            return None
        section = {}

        line = csv_iterator.__next__()
        section['title'] = line['Summary']

        num_paras = RAND_PAR.randint(1, MAX_PAR)
        paras = []
        for i in range(num_paras):
            line = csv_iterator.__next__()
            paras.append(line['Text'])

        section['paragraphs'] = paras

        num_figures = RAND_PAR.randint(1, num_paras + 1)
        figures = []
        for i in range(num_figures):
            index = np.random.randint(len(urls))
            figures.append({"URL": urls[index]['image_URL'], "caption": captions[index]['caption']})

        section['figures'] = figures

        # Add figures

        if level < max_depth:
            subsections = []
            for i in range(RAND_SUBSECTIONS.randint(1, MAX_SUBSECTION)):
                subsections.append(create_section(csv_iterator, urls, captions, level + 1, max_depth))

            section['subsections'] = subsections

        return section
    except StopIteration:
        raise StopIteration


if sys.argv is not None and len(sys.argv) > 1:
    if sys.argv[1] is not None:
        out_file = in_file = sys.argv[1]
    if sys.argv[2] is not None:
        out_file = sys.argv[2]

    add_sections(in_file, out_file)
    author.email_bio_date_adder(out_file, out_file)
    print("Done!")
else:
    print("Too few arguments")
