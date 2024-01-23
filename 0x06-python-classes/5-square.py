#!/usr/bin/python3
"""ddddddddddddddddddddddddddddddddddddddddddddddddddd
ddddddddddddddd dddddddddddddddd ddddd
"""


class Square:
    """sk sssssssss sssssss sssssss s
    """
    def __init__(self, size=0):
        """sd dddddddddddddd ddddddddddd
        """
        self.size = size

    def area(self):
        """dddddddddd dddddddddd dddddd
        """
        return (self.__size ** 2)

    @property
    def size(self):
        """ssssssssss ssssssssssssss sssssss
        """
        return (self.__size)

    @size.setter
    def size(self, value):
        """sssssssss ss ssssss sssssssssssssssssssssss
        sssssssss
        """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    def my_print(self):
        """sssss ssssssss ssssssssssssssssssss sssss
        ssssssssssssssssss
        """
        if (self.__size == 0):
            print("")
        else:
            for i in range(self.__size):
                for j in range(self.__size):
                    print("#", end="")
                print("", end="\n")
