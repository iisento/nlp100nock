import unittest
import knock00

class TestKnock00(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(knock00.reverse_string("あいうえお"), "おえういあ")
