import unittest

from Calculator.calculator import Calculator;
from Calculator.statistics import Statistics;



class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()
        self.statistics = Statistics()

    def test_calculator_return_sum(self):
        result = self.calculator.Sum(1, 2)
        self.assertEqual(3, result)


    def test_calculator_return_Product(self):
        result = self.calculator.Product(2, 4)
        self.assertEqual(8, float(result))

    def test_statistics_calculator_return_mean(self):
        data = [1, 2, 3, 4, 5]
        result = self.statistics.mean(data)
        self.assertEqual(3, result)

if __name__ == '__main__':
    unittest.main()