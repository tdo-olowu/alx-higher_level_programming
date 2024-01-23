#!/usr/bin/python3
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    def __str__(self):
        self.my_print()

    def area(self):
        return (self.__size ** 2)

    @property
    def size(self):
        return (self.__size)

    @property
    def position(self):
        return (self.__position)

    @size.setter
    def size(self, value):
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        if (type(value) is not tuple):
            raise TypeError
        a = value[0]
        b = value[1]
        if ((type(a) is not int) or (type(b) is not int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        if (self.__size == 0):
            print("", end='\n')
        else:
            pad_a = self.__position[0]
            for i in range(self.__size):
                print(" " * pad_a, end="")
                print("#" * self.__size)
        print("")
