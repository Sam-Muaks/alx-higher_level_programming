#!/usr/bin/python3
"""Script that assigns a private instance attribute size to class
    Square with size validation"""

class Square:
    """Class that defines a square with a private instance attribute size"""

    def __init__(self, size=0):
        """Initiates a new square.
        Args:
        size (int): The size of the new square.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
