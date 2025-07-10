import unittest

import calculator

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(calculator.add(11,12),23)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(20,8),12)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(20,4),80)

    def test_divide(self):
        self.assertEqual(calculator.divide(20,2),10)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculator.divide(1,0)

