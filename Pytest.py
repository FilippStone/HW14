from doctest_01 import fibonacci
import pytest

def test_fibonacci():
    assert list(fibonacci(0)) == [1, 1]
    assert list(fibonacci(1)) == [1, 1]
    assert list(fibonacci(2)) == [1, 1]
    assert list(fibonacci(10)) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

if __name__ == '__main__':
    pytest.main()
