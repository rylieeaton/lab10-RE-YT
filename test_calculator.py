# https://github.com/rylieeaton/lab10-RE-YT  
# Partner 1: Rylie Eaton
# Partner 2: Yasmin Tatari

import unittest
from calculator import *


class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):  # 3 assertions
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):  # 3 assertions
        self.assertEqual(subtract(5, 3), 2)
        self.assertEqual(subtract(3, 5), -2)
        self.assertEqual(subtract(10, 10), 0)

    ##########################

    ######## Partner 1
    def test_multiply(self): # 3 assertions
        self.assertEqual(mul(2, 2), 4)
        self.assertEqual(mul(2, 3), 6)
        self.assertEqual(mul(2, 4), 8)

    def test_divide(self): # 3 assertions
        self.assertEqual(div(2, 6), 3)
        self.assertEqual(div(3, 6), 2)
        self.assertEqual(div(5, 10), 2)

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self):  # 3 assertions
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(2, 8), 3)
        self.assertAlmostEqual(logarithm(10, 1000), 3)

    def test_log_invalid_base(self):  # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(-1, 10)
    ##########################

    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(2, -10)

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(3, 6), 6.708203932499369)
        self.assertAlmostEqual(hypotenuse(3, 8), 8.54400374531753)

    def test_sqrt(self): # 3 assertions
        self.assertEqual(square_root(4), 2)
        self.assertAlmostEqual(square_root(2), 1.4142135623730951)
        self.assertAlmostEqual(square_root(9), 3)
        
        with self.assertRaises(ValueError):
            square_root(-4)
    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()
