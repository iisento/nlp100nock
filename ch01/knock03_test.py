import unittest
import knock03


class TestKnock03(unittest.TestCase):
    def test_generate_pi(self):
        self.assertEqual(knock03.generate_pi(), [
                         3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5, 8, 9, 7, 9])
