from mul_div import Lexer, Interpreter
import pytest


@pytest.mark.parametrize("input_string, expected_result",[
    ("7 * 4 / 2",14),
    ("7 * 4 / 2 * 3",42),
    ("10 * 4  * 2 * 3 / 8",30),
])

def test_multiplication_division(input_string,expected_result):
    lexer = Lexer(input_string)
    interpreter = Interpreter(lexer)
    result = interpreter.expr()
    assert result == expected_result