#!/usr/bin/python3
"""tests for the Base class
"""


import sys
sys.path.append("../../")
import unittest


class Test_Rectangle(unittest.TestCase):
    """class for testing the Rectangle class"""
    def setUp(self):
        dummyr = __import__("rectangle").Rectangle
        dummyr = dummyr(2, 2)
