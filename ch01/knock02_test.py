import unittest
import knock02


class TestKnock02(unittest.TestCase):
    def test_concatenate_words(self):
        self.assertEqual(knock02.concatenate_words("パトカー", "タクシー"), "パタトクカシーー")
