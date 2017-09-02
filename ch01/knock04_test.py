import unittest
import knock04


class TestKnock04(unittest.TestCase):
    def test_generate_atoms(self):
        atoms_dict = {
            1: 'H', 2: 'He', 3: 'Li', 4: 'Be', 5: 'B',
            6: 'C', 7: 'N', 8: 'O', 9: 'F', 10: 'Ne',
            11: 'Na', 12: 'Mi', 13: 'Al', 14: 'Si', 15: 'P',
            16: 'S', 17: 'Cl', 18: 'Ar', 19: 'K', 20: 'Ca'}
        self.assertEqual(knock04.generate_atoms(), atoms_dict)
