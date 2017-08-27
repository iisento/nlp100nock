import unittest
from knock05 import NGram
from knock06 import BiGramSet


class TestKnock06(unittest.TestCase):

    def test_BiGramSet(self):
        BG = BiGramSet('paraparaparadise', 'paragraph')
        se = ['s', 'e']
        union_XY = set([frozenset(['a', 'r']), frozenset(['i', 's']),
                        frozenset(['d', 'i']), frozenset(['a', 'd']),
                        frozenset(['a', 'p']), frozenset(['a', 'g']),
                        frozenset(['e', 's']), frozenset(['g', 'r']),
                        frozenset(['h', 'p'])])
        diff_XY = set([frozenset(['a', 'd']), frozenset(['i', 's']),
                       frozenset(['e', 's']), frozenset(['d', 'i'])])
        self.assertEqual(BG.union(), union_XY)
        self.assertEqual(BG.difference(), diff_XY)
        self.assertEqual(BG.contain('se'), True)
