#!/usr/bin/python3
"""Define singly linked list"""


class Node:
    """Node class for singly linked list"""

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get data of node"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set data of node"""
        if not isinstance(value, int):
            raise TypeError('data must be an integer')
        self.__data = value

    @property
    def next_node(self):
        """Get next node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set next node"""
        if not isinstance(value, Node) and value is not None:
            raise TypeError('next_node must be a Node object')
        self.__next_node = value


class SinglyLinkedList:
    """Singly linked list class"""

    def __init__(self):
        self.__head = None

    def __str__(self):
        """String representation of singly linked list"""
        string = ''
        current = self.__head
        while current:
            string += str(current.data) + '\n'
            current = current.next_node
        return string.strip()

    def sorted_insert(self, value):
        """Inserts a node in sorted order

        Args:
            value (int): value to insert
        """
        new = Node(value)
        if self.__head is None:
            self.__head = new
            return
        if value < self.__head.data:
            new.next_node = self.__head
            self.__head = new
            return
        current = self.__head
        while current.next_node and current.next_node.data < value:
            current = current.next_node
        new.next_node = current.next_node
        current.next_node = new
