#!/usr/bin/python3
"""Script that assigns a private instance attribute size to a class square"""

class Square:
    """Class that defines a square with a private instance attribute size"""

    def __init__(self, size):
        """Initiates a new square
        Args:
            size (int): The size of the new square.
            """
        self.__size = size
