import unittest
from doctest_01 import fibonacci


class TestFibonacci(unittest.TestCase):

    def test_fibonacci_zero(self):
        self.assertEqual(list(fibonacci(0)), [1, 1])

    def test_fibonacci_one(self):
        self.assertEqual(list(fibonacci(1)), [1, 1])

    def test_fibonacci_two(self):
        self.assertEqual(list(fibonacci(2)), [1, 1])

    def test_fibonacci_ten(self):
        self.assertEqual(list(fibonacci(10)), [1, 1, 2, 3, 5, 8, 13, 21, 34, 55])

if __name__ == '__main__':
    unittest.main()

