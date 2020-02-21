
# ABSTRACTION

from MathOperations.Addition import Addition;
from MathOperations.Multiplication import Multiplication;

class Calculator:
    Result = 0

    def __init__(self):
        pass
    def Sum(self, a, b):
        self.Result = Addition.sum(a, b)
        return self.Result

    def Product(self, a, b):
        self.Result = Multiplication.product(a, b)
        return self.Result






