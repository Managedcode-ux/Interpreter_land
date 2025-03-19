from calc1 import Interpreter
import pytest


def test_addition():
    interpreter = Interpreter("3+5")
    result = interpreter.expr()
    assert result == 8


@pytest.mark.parametrize("input_string, expected_result", [
    ("13+5", 18),
    ("5+13", 18),
    ("123+4", 127),
    ("4+123", 127),
    ("123+456", 579),
    ("123 + 4", 127),
])
def test_multivalue_addition(input_string, expected_result):
    interpreter = Interpreter(input_string)
    result = interpreter.expr()
    assert result == expected_result


@pytest.mark.parametrize("input_string, exp_res")([
    ("1*3", 3),
    ("2*12", 24),
    ("12*2", 24),
    ("12*12", 144),
    ("100*100", 10000)
])
def test_multivalue_multiplication(input_string, exp_res):
    interpreter = Interpreter(input_string)
    result = interpreter.expr()
    assert result == exp_res


@pytest.mark.parametrize("input_string, exp_res")([
    ("1%3", "invalid exp"),
    ("2%12", "invalid exp"),
    ("12%2", 0),
    ("12%12", 0),
    ("100%100", 0)
])
def test_multivalue_division(input_string, exp_res):
    interpreter = Interpreter(input_string)
    result = interpreter.expr()
    assert result == exp_res
