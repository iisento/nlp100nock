import unittest
from knock09 import typoglycemia


class TestKnock09(unittest.TestCase):

    def test_typoglycemia(self):
        s = ("I couldn't believe that I could actually understand "
             "what I was reading : the phenomenal power of the human mind .")
        ss = typoglycemia(s, seed=0)
        ss_answer = (
            "I cd'oulnt bevelie that I culod aalctuly uanrnetdsd "
            "what I was rineadg : the pnaohneeml pweor of the hmaun mind .")
        self.assertEqual(ss, ss_answer)
