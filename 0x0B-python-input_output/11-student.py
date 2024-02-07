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

    def to_json(self, attrs=None):
        """Expresses a class in serialisable form
        Args:
            attrs (any): should have serialisable attrs
        Return:
            the serialisable string of the object
        """
        if (attrs is None):
            dct_repr = {"first_name": self.first_name,
                        "last_name": self.last_name,
                        "age": self.age
                        }
        else:
            dct_repr = {}
            for attr in attrs:
                if hasattr(self, attr):
                    dct_repr[attr] = getattr(self, attr)
        return (dct_repr)

    def reload_from_json(self, json):
        """replaces all attributes of the Student instance
        with the json dictionary representation
        """
        for attr, val in json.items():
            if hasattr(self, attr):
                setattr(self, attr, val)
