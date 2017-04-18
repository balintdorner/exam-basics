import unittest
from odd_avg import *

class TestOddAvg(unittest.TestCase):
    def test_odd_average_empt_list(self, integer = []):
        odd_avg = OddAvg()
        integer = []
        self.assertEqual(odd_avg.odd_average(integer), 0)

    def test_odd_average_only_odd(self, integer = []):
        odd_avg = OddAvg()
        integer = [2, 6, 10]
        self.assertEqual(odd_avg.odd_average(integer), 6)

    def test_odd_average_integers(self, integer = []):
        odd_avg = OddAvg()
        integer = [1, 2, 3, 7, 12, 16]
        self.assertEqual(odd_avg.odd_average(integer), 10)


if __name__ == '__main__':
    unittest.main()
