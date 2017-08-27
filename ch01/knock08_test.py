import unittest
from knock08 import cipher


class TestKnock08(unittest.TestCase):

    def test_cipher(self):
        s = 'aoBeghaAwAoeh'
        ciphered = cipher(s)
        ciphered_answer = '97111B10110310497A119A111101104'
        self.assertEqual(ciphered, ciphered_answer)
