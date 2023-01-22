from re import sub, search


def rm_incorrect_issn(ifile_nm, ofile_nm):
    with open(ifile_nm) as ifile:
        nw_lines = []
        for line in ifile.readlines():
            line = sub(r'NumberInt\(([0-9]+)\)', r'\1', line)
            match = search(r'"issn"[ ]*:[ ]*"(?![0-9]{4}-[0-9]{4}")', line)
            if match:
                # if it matches, then the lookahead is not considered, and we close the
                # string with the eol, checking if it ends with , or not
                try:
                    eol = search(r'(?<=")[,]*[ \t]*$', line)
                    nw_lines.append(match.group() + '"' + eol.group() + '\n')
                except:
                    print(line)
            else:
                nw_lines.append(line)

    with open(ofile_nm, 'w') as ofile:
        ofile.writelines(nw_lines)
        ofile.flush()
