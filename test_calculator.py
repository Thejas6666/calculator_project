import unittest
import sys
import calculator
import HtmlTestRunner

class TestCalculator(unittest.TestCase):

    def setUp(self):
        print("Running setup")
        self.a=10
        self.b=2

    def tearDown(self):
        print("Running teardown")

    def test_add(self):
        result=calculator.add(self.a,self.b)
        self.assertEqual(result,12)

    def test_subtract(self):
        result=calculator.subtract(self.a,self.b)
        self.assertEqual(result,8)

    def test_multiply(self):
        result=calculator.multiply(self.a,self.b)
        self.assertEqual(result,20)

    def test_divide(self):
        result=calculator.divide(self.a,self.b)
        self.assertEqual(result,5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            calculator.divide(1,0)

    @unittest.skip("Skipping temporarily")
    def test_skip_test(self):
        self.name="Thejas"
        self.assertEqual(self.name,"Thejas")

    @unittest.skipIf(sys.platform.startswith("win"),"Does not run on windows")
    def test_unix_addition(self):
        result=calculator.add(self.a,self.b)
        self.assertEqual(result,12)

if __name__ == '__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='test_reports'))
