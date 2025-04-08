import pytest
from calculator import Calculator

calc = Calculator()

def test_addition():
    assert calc.evaluate("2+3") == "5.0"

def test_subtraction():
    assert calc.evaluate("10-4") == "6.0"

def test_multiplication():
    assert calc.evaluate("3*5") == "15.0"

def test_division():
    assert calc.evaluate("8/2") == "4.0"

def test_operator_precedence():
    assert calc.evaluate("2+3*4") == "14.0"

def test_parentheses():
    assert calc.evaluate("(2+3)*4") == "20.0"
    assert calc.evaluate("2+3)") == "Error"
    assert calc.evaluate("(2+3") == "Error"

def test_nested_parentheses():
    assert calc.evaluate("((1+2)*3)+4") == "13.0"

def test_decimal():
    assert calc.evaluate("2.5*4") == "10.0"

def test_division_by_zero():
    assert calc.evaluate("10/0") == "Error"

def test_invalid_expression():
    assert calc.evaluate("5++2") == "Error"


