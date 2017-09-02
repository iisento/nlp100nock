import unittest
from knock10 import count_lines


class TestKnock10(unittest.TestCase):

    def test_count_lines(self):
        lines_answer = 24
        lines = count_lines("./hightemp.txt")
        self.assertEqual()
