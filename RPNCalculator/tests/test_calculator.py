import unittest

from RPNCalculator import Calculator


class TestCalc(unittest.TestCase):
    def setUp(self):
        self.calculator = Calculator()

    def tearDown(self):
        self.calculator.clear()

    def test_simple_input(self):
        val = self.calculator.input("5")
        self.assertEqual(val, "5", "Should be 5")

    def test_complex_input(self):
        val = self.calculator.input("5 5 5 8 + + -")
        self.assertEqual(val, "-13.0", "Should be -13.0")


if __name__ == "__main__":
    unittest.main()
