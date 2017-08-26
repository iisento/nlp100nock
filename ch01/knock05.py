class NGram:

    def __init__(self, sentence):
        self._sentence = sentence

    def word(self, dim=2, type='list'):
        s_list = self._sentence.split()
        s_list_len = len(s_list)
        s_lists = []
        for i in range(dim):
            s_lists.append(s_list[i: s_list_len - (1 - i)])
        if type == 'list':
            return [list(s) for s in zip(*s_lists)]
        elif type == 'set':
            return {frozenset(s) for s in zip(*s_lists)}

    def char(self, dim=2, type='list'):
        s = self._sentence.replace(' ', '')
        s_len = len(s)
        s_list = []
        for i in range(dim):
            s_list.append(s[i: s_len - (i - 1)])
        if type == 'list':
            return [list(s) for s in zip(*s_list)]
        elif type == 'set':
            return {frozenset(s) for s in zip(*s_list)}
