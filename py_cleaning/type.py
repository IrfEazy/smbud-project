from json import load, dump


def check_book(data):
    try:
        if data["isbn"] != "" and data["isbn"] is not None:
            data["publication_type"] = "Book"
            return True
    except:
        return False


def check_journal(data):
    try:
        if (data["volume"] != "" and data["volume"] is not None) or (
                data["issue"] != "" and data["issue"] is not None) or (data["issn"] != "" and data["issn"] is not None):
            data["publication_type"] = "Journal"
            return True
    except:
        return False


def type_adder(in_file, out_file):
    with open(in_file) as f:
        data = load(f)

    count = 0
    for i in range(len(data)):
        count += 1
        if not check_book(data[i]):
            if not check_journal(data[i]):
                data[i]["publication_type"] = "Conference"

    with open(out_file, 'w') as f:
        dump(data, f, indent=4)

    print("done ", count)
