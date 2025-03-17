from calc1 import Interpreter
import pytest


def test_addition():
    interpreter = Interpreter("3+5")
    result = interpreter.expr()
    assert result == 8


@pytest.mark.parametrize("input_string, expected_result", [
    ("13+5", 18),
    ("5+13", 18),
    ("123+4",127)
])
def test_multivalue_addition(input_string, expected_result):
    interpreter = Interpreter(input_string)
    result = interpreter.expr()
    assert result == expected_result
