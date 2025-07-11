import unittest
import calculator

class TestDivide(unittest.TestCase):
    def test_divide(self):

        self.assertEqual(calculator.divide(3,3),1)