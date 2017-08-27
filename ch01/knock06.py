from knock05 import NGram


class BiGramSet:

    def __init__(self, s1, s2,):
        self._X = NGram(s1).char(2, type='set')
        self._Y = NGram(s2).char(2, type='set')

    def union(self):
        return self._X | self._Y

    def difference(self):
        return self._X - self._Y

    def contain(self, Z):
        if isinstance(Z, str):
            Z = {z for z in Z}
        return Z in self._X
