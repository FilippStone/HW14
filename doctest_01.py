def fibonacci(n):
    """
    Генератор чисел Фибоначчи, начинается 1, 1 + n...

    >>> list(fibonacci(10))
    [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]

    >>> list(fibonacci(1))
    [1]

    >>> list(fibonacci(2))
    [1, 1]

    >>> list(fibonacci(0))
    []
    """
    n1, n2 = 1, 1
    yield n1
    yield n2
    for i in range(n - 2):
        n1, n2 = n2, n1 + n2
        yield n2

# Doctest
if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose=True)

