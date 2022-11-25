import pytest
from app.calculator import Calculator


class testcalc:
    def setup(self):
        self.calc = Calculator

def test_multiply_calculate_correctly(self):
    assert self.calc.multiply(self, 3, 3) == 9

def test_division_calculate_correctly(self):
    assert self.calc.division(self, 300, 3) == 100

def test_subtraction_calculate_correctly(self):
    assert self.calc.subtraction(self, 27, 3) == 24

def test_adding_calculate_correctly(self):
    assert self.calc.adding(self, 27, 3) == 30

