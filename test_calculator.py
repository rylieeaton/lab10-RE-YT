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
        self.assertEqual(mul(2,2),4)
        self.assertEqual(mul(2,3),6)
        self.assertEqual(mul(2,4),8)


    def test_divide(self): # 3 assertions
        self.assertEqual(div(6,2), 3)
        self.assertEqual(div(6,3), 2)
        self.assertEqual(div(10,5), 2)

    ######## Partner 2
    def test_divide_by_zero(self):  # 1 assertion
        # call division function inside, example:
        # with self.assertRaises(<INSERT_ERROR_TYPE>):
        #     div(0, 5)
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self):  # 3 assertions
        self.assertAlmostEqual(logarithm(10, 100), 0.5)
        self.assertAlmostEqual(logarithm(2, 8), 0.33333333333333337)
        self.assertAlmostEqual(logarithm(10, 1000), 0.33333333333333337)

    def test_log_invalid_base(self):  # 1 assertion
        # use same technique from test_divide_by_zero
        with self.assertRaises(ValueError):
            logarithm(1, -10)
    ##########################

    ######## Partner 1
    def test_log_invalid_argument(self): # 1 assertion
    #     # call log function inside, example:
        with self.assertRaises(ValueError):
            logarithm(0, 7)
    #     fill in code

    def test_hypotenuse(self): # 3 assertions
        self.assertEqual(hypotenuse(3,4),5)
        self.assertAlmostEqual(hypotenuse(3,6),6.708203932499369)
        self.assertAlmostEqual(hypotenuse(3,8),8.54400374531753)

    def test_sqrt(self): # 3 assertions
    #     # Test for invalid argument, example:
        with self.assertRaises(ValueError):
            square_root(-4)
    #     # Test basic function
    #     fill in code
    ##########################


# Do not touch this
if __name__ == "__main__":
    unittest.main()