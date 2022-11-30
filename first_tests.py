import pytest
from app.Calculator import Calculator

class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply_calculate_correcltly(self):
        assert self.calc.multiply(self, 2, 5) == 10

    def test_multiply_calculate_failed(self):
        assert self.calc.multiply(self, 2, 5) == 12

    def test_division_calculate_correcltly(self):
        assert self.calc.division(self, 10, 5) == 2

    def test_division_calculate_failed(self):
        assert self.calc.division(self, 10, 5) == 3

    def test_subtraction_calculate_correcltly(self):
        assert self.calc.subtraction(self, 10, 5) == 5

    def test_subtraction_calculate_failed(self):
        assert self.calc.subtraction(self, 10, 5) == 6

    def test_adding_calculate_correcltly(self):
        assert self.calc.adding(self, 2, 5) == 7

    def test_adding_calculate_failed(self):
        assert self.calc.adding(self, 2, 5) == 9
