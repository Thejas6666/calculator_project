import unittest
import calculator

class TestSubtract(unittest.TestCase):
    def test_subtract(self):
        self.assertEqual(calculator.subtract(3,3),0)