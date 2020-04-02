import string
import unittest

def namelist(names):
    i = 1;
    res = ""
    l_names = []

    for n in names:
        l_names.append(n['name'])
    l = len(l_names)
    for name in l_names:
        res += name
        if i < l - 1:
            res += ", "
        elif i == l - 1:
            res += " & "
        i += 1

    print(res)
    return (res)

namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}]),

