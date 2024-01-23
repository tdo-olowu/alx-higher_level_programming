#!/usr/bin/python3
"""aksj nsla wkwlk dwlnwld wldknlwdlwdnlwdbjkablkabla
"""


class Square:
    """asaslknsal alksnlsaknlas lkasnlaskn lkasnlsaknd
    """
    def __init__(self, size=0, position=(0, 0)):
        """skljans laksnsal lkasnsal lksanl """
        self.size = size
        self.position = position

    def area(self):
        """asn alsnlsan lkasnlksanlksa aslknwlnl"""
        return (self.__size ** 2)

    @property
    def size(self):
        """sakjln lasknsal wlknwlkwn leknlw lkwenl
        """
        return (self.__size)

    @property
    def position(self):
        """asklnlsak alskas
        aslkas
        """
        return (self.__position)

    @size.setter
    def size(self, value):
        """klsk lksl aslk aslklas salkelkelk elknedlknedl
        KLJnkle nlednlken
        """
        if (type(value) is not int):
            raise TypeError("size must be an integer")
        elif (value < 0):
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """these comments jare tedious to type, esp when pressing matters
        are pressing
        """
        if (type(value) is not tuple):
            raise TypeError
        elif (len(value) > 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        a = value[0]
        b = value[1]
        if ((type(a) is not int) or (type(b) is not int)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """sssssssssssssss
        ssssssssssss
        """
        if (self.__size == 0):
            print("", end='\n')
        else:
            pad_a = self.__position[0]
            pad_b = self.__position[1]
            for i in range(self.__size):
                if (pad_b == 0):
                    print(" " * pad_a, end="")
                print("#" * self.__size)
        print("")
