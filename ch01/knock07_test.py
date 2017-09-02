import unittest
from knock07 import to_sentence


class TestKnock07(unittest.TestCase):

    def test_to_sentence(self):
        x, y, z = 12, '気温', 22.4
        s = to_sentence(x, y, z)
        s_answer = '12時の気温は22.4'
        self.assertEqual(s, s_answer)
