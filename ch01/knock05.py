class NGram:

    def __init__(self, sentence):
        self._sentence = sentence

    def word(self, dim):
        i = dim - 1
        s_list = self._sentence.split()
        s_list1 = s_list[:-i]
        s_list2 = s_list[i:]
        return [list(s) for s in zip(s_list1, s_list2)]

    def char(self, dim):
        i = dim - 1
        s = self._sentence.replace(' ', '')
        s1 = s[:-i]
        s2 = s[i:]
        return [list(s) for s in zip(s1, s2)]
