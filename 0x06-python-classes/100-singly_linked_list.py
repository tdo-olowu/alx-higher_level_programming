#!/usr/bin/python3

class Node:
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        return self.__data
    @property
    def next_node(self):
        return self.__next_node

    @data.setter
    def data(self, value):
        if (type(value) is not int):
            raise TypeError("data must be an integer")
        self.__data = value
    @next_node.setter
    def next_node(self, value):
        if ((value is None) or (type(value) is Node)):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")



class SinglyLinkedList:
    def __init__(self):
        self.__head = Node(0, None)

    def __str__(self):
        temp = self.__head
        while (temp is not None):
            print(temp.data)
            temp = temp.next_node

    def sorted_insert(self, value):
        pass
