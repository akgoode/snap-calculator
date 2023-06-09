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

    def test_multiple_inputs(self):
        inputs = "3 5 + 10 -"
        result = ""
        for val in inputs.split(" "):
            result = self.calculator.input(val)

        self.assertEqual(result, "-2.0", "Should be -2")

    def test_clear(self):
        self.calculator.input("c")
        self.assertEqual(
            str(self.calculator), "[ ]", "Should be an empty array with a space inside."
        )

    def test_addition(self):
        result = self.calculator.input("5 5 +")
        self.assertEqual(result, "10.0", "Should be 10")

    def test_subtraction(self):
        result = self.calculator.input("25 5 -")
        self.assertEqual(result, "20.0", "Should be 20")

    def test_multiplication(self):
        result = self.calculator.input("5 5 *")
        self.assertEqual(result, "25.0", "Should be 25")

    def test_division(self):
        result = self.calculator.input("12 4 /")
        self.assertEqual(result, "3.0", "Should be 3")


if __name__ == "__main__":
    unittest.main()
