def readfile(filename):
    result = {}
    with open(filename, "r") as f:
        for line in f:
            langs = line.rstrip().split(":")
            if langs[0] in result:
                result[langs[0]].append(langs[1])
            else:
                result[langs[0]] = [langs[1]]
    f.close()

    return result