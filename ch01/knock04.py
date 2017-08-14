import re


def generate_atoms():
    s1 = ('Hi He Lied Because Boron Could Not Oxidize Fluorine.'
          ' New Nations Might Also Sign Peace Security Clause. '
          'Arthur King Can.')
    s2 = re.sub(',|\.', '', s1).split()
    wl = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    res = {}
    i = 1
    for s in s2:
        if i in wl:
            res[i] = s[0:1:1]
        else:
            res[i] = s[0:2:1]
        i += 1
    return res
