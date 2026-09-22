import pytest

from app.calculator import add, divide, multiply, subtract


@pytest.mark.parametrize(
    "a, b, expected",
    [(1, 2, 3), (-1, 1, 0), (0, 0, 0), (2.5, 2.5, 5.0)],
)
def test_add(a, b, expected):
    assert add(a, b) == expected


def test_subtract():
    assert subtract(5, 3) == 2


def test_multiply():
    assert multiply(4, 3) == 12


def test_divide():
    assert divide(10, 4) == 2.5


def test_divide_by_zero():
    with pytest.raises(ValueError):
        divide(1, 0)
