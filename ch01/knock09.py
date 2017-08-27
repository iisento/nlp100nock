import random


def typoglycemia(s, seed=None):
    list = s.split()
    list2 = [wtypoglycemia(w, seed) for w in list]
    return ' '.join(list2)


def wtypoglycemia(word, seed):
    random.seed(seed)
    if len(word) < 5:
        return word
    else:
        wl = [w for w in word]
        wll = wl[1: -1]
        wl[1: -1] = random.sample(wll, len(wll))
        return ''.join(wl)
