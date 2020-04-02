def duplicate_count(text):
    d = {}
    i = 1
    for a in text:
        if d.get(a.lower()) == None:
           d[a.lower()] = 1
        else:
            d[a.lower()] += 1
        #print("| "+ a + " |\n")
    res = 0
    s = 0
    for a in d:
        #print(a, end = ' ')
        if d[a] > 1:
            res += 1
    print(res)
    return (res)

duplicate_count("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
