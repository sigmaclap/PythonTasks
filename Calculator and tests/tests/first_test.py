import pytest
from app.calculator import Calculator

class TestCalculator:
    def setup(self):
        self.calculator = Calculator()

    def test_multiple_correct(self):
        assert self.calculator.multiply(2, 2) == 4

    def test_multiple_fail(self):
        assert self.calculator.multiply(2, 2) == 5
