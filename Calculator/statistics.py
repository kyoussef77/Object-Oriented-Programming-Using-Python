from Calculator.calculator import Calculator
from MathOperations.mean import Mean

class Statistics(Calculator):

    def mean(self, data):
        self.Result = Mean(data)
        return self.Result
