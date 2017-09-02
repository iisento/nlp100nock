def cipher(s):
    return ''.join(ccipher(i) for i in s)


def ccipher(s):
    return str(ord(s)) if s.islower() else s
