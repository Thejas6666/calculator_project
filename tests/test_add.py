import unittest
import calculator

class TestAdd(unittest.TestCase):
    def test_add(self):
        test_cases=[(1,3,4),(-21,20,-1),(-1,-1,-2),(20,-2,18)]
        for a,b,expected in test_cases:
            with self.subTest(a=a,b=b,expected=expected):
                self.assertEqual(calculator.add(a,b),expected)