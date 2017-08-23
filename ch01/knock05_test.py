import unittest
import knock05


class TestKnock05(unittest.TestCase):
    def test_n_gram(self):
        sample_sentence = 'I am an NLPer'
        n_gram = knock05.NGram(sample_sentence)
        word_bi_gram = n_gram.word(2)
        char_bi_gram = n_gram.char(2)
        word_bi_gram_answer = [['I', 'am'], ['am', 'an'], ['an', 'NLPer']]
        char_bi_gram_answer = [['I', 'a'], ['a', 'm'], ['m', 'a'],
                               ['a', 'n'], ['n', 'N'], ['N', 'L'],
                               ['L', 'P'], ['P', 'e'], ['e', 'r']]
        self.assertEqual(word_bi_gram, word_bi_gram_answer)
        self.assertEqual(char_bi_gram, char_bi_gram_answer)
