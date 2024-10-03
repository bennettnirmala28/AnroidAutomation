import unittest
from AndroidAutomation.pages.calculator_page import CalculatorPage


class CalculatorTest(unittest.TestCase):
    def setUp(self):
        # Initialize the calculator page
        self.calculator = CalculatorPage()

    def test_addition(self):
        # Perform the addition: 2 + 3 = 5
        self.calculator.press_2()
        self.calculator.press_plus()
        self.calculator.press_3()
        self.calculator.press_equal()
        self.calculator.get_result()

        # Verify the result
        result = self.calculator.get_result()
        self.assertEqual(result, '5')


    def tearDown(self):
    # Quit the Appium driver
     self.calculator.quit()


if __name__ == "__main__":
    unittest.main()
