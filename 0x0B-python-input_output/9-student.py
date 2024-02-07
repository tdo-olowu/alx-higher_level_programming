#!/usr/bin/python3
"""student representation
"""


class Student():
    """a student class
    """
    def __init__(self, first_name, last_name, age):
        """initialiser"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Expresses a class in serialisable form
        Args:
            obj (any): should have serialisable attrs
        Return:
            the serialisable string of the object
        """
        dct_repr = {"first_name": self.first_name,
                    "last_name": self.last_name,
                    "age": self.age
                    }
        return (dct_repr)
