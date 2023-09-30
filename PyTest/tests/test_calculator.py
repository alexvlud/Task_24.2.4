import pytest
from app.calculator import Calculator


class TestCalc:
    def setup(self):
        self.calc=Calculator

    def test_adding_success(self):
        assert self.calc.adding(self,1,2)==3


    def test_subtraction(self):
        assert self.calc.subtraction(self,13,3)==10

    def test_division(self):
        assert self.calc.division(self, 22, 11)==2

    def test_multiply(self):
        assert self.calc.multiply(self, 13, 2)==26


    def teardown(self):
        print('Выполнение метода Teardown')
