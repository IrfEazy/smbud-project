import json


def checkBook(data):
    try:
        if data["isbn"] != "" and data["isbn"] is not None:
            data["publication_type"] = "Book"
            return True
    except: 
        return False


def checkJournal(data):
    try:
        if (data["volume"] != "" and data["volume"] is not None) or (data["issue"] != "" and data["issue"] is not None) or (data["issn"] != "" and data["issn"] is not None):
            data["publication_type"] = "Journal"
            return True
    except: 
        return False


def typeAdder(in_file, out_file):
    with open(in_file) as f:
        data = json.load(f)

    count = 0
    for i in range(len(data)):
        count += 1
        if not checkBook(data[i]):
            if not checkJournal(data[i]):
                data[i]["publication_type"] = "Conference"

    with open(out_file, 'w') as f:
        json.dump(data, f, indent=4)

    print("done ", count)










