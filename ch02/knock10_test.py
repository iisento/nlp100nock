import unittest
from knock10 import count_lines


class TestKnock10(unittest.TestCase):

    def test_count_lines(self):
        lines = count_lines("./hightemp.txt")
        lines_answer = 24       # calculated by wc command
        self.assertEqual(lines, lines_answer)
