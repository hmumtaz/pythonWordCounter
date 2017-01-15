def count(textfile):
    file = open(textfile, "r")
    fileText = file.read()
    fileText = fileText.capitalize()
    dict = {}
    for word in fileText.split():
        if word not in dict:
            dict[word] = 1
        else:
            dict[word] += 1
    sortedDict = [(k, dict[k]) for k in sorted(dict, key=dict.get, reverse=True)]
    print("Top Word:", sortedDict[0])



count(**YOUR TEXT FILE HERE**)
