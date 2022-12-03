from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc = Calculator

    def test_multiply(self):
        assert self.calc.multiply(self, 2, 2) == 4

    def test_division(self):
        assert self.calc.division(self, 10, 2) == 5

    def test_subtraction(self):
        assert self.calc.subtraction(self, 10, 5) == 5

    def test_adding(self):
        assert self.calc.adding(self, 1, 1) == 2

