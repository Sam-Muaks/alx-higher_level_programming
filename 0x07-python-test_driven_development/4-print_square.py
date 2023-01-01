#!/usr/bin/python3
"""Print square module"""

def print_square(size):
    """
    function that prints a square with the character '#'

    @size: length of the square
    """

    if not isinstance(size, int) and not isinstance(size, float):
        raise TypeError('size must be an integer')
    if size < 0:
        raise ValueError('size must be >= 0')
    if isinstance(size, float), and size < 0:
        raise TypeError('size must be an integer')
    if isinstance(size, float):
        size = int(size)
    for i in range(size):
        print('#' * size)
