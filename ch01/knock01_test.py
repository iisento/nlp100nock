import unittest
import knock01

class TestKnock01(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(knock01.split_patato("パタトクカシーー", 0), "パトカー")
        self.assertEqual(knock01.split_patato("パタトクカシーー", 1), "タクシー")

if __name__ == "__main__":
    unittest.main()
