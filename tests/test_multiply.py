import unittest
import calculator

class TestMultiply(unittest.TestCase):
    def test_multiply(self):
        self.assertEqual(calculator.multiply(2,3),6)