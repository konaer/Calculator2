###################
# Dejing Kong
# IS606 project2
###################

from Calculator.Subtraction import subtraction
from Calculator.Addition import addition
from Calculator.Multiplication import multiplication
from Calculator.Division import division
from Calculator.Square import squaring
from Calculator.SquareRoot import squarerooting



class Calculator:
    result = 0
    data = []

    def __init__(self):
        pass

    def add(self, a, b):
        self.result = addition(a, b)
        return self.result

    def subtract(self, a, b):
        self.result = subtraction(a, b)
        return self.result

    def multiply(self, a, b):
        self.result = multiplication(a, b)
        return self.result

    def divide(self, a, b):
        self.result = round(dividing(a, b), 9)
        return self.result

    def square(self, a):
        self.result = squaring(a)
        return self.result

    def square_root(self, a):
        self.result = round(square_rooting(a), 8)
        return self.result
