#!/usr/bin/python3
""" Creates an empty class called Square
"""
class Square:
    """ Empty class with size private attribute
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Instantiation with size
        Args:
        size: size of the square
        position: postion of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        self.position = position

        def area(self):
            """
            Returns the area of the square
            """
            return (self.__size * self.__size)

        @property
        def size(self):
            """
            size getter. Handle size errors
            """
            return self.__size

        @size.setter
        def size(self, value):
            """
            size setter. Set the size square
            """
            if type(value) is not int:
                raise TypeError("size must be an integer")
            if value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

            def my_print(self):
                """
                Print a square with the character # at position given
                """
                if self.__size == 0:
                    print()
                    return
                for j in range(self.__position[1]):
                    print()
                    for i in range(self.__size):
                        print(" " * self.__position[0], end="")
                        print("#" * self.__size)

                        @property
                        def position(self):
                            """
                            position setter. Set the position of square
                            """
                            return self.__position

                        @position.setter
                        def position(self, value):
                            """
                            Handle position with errors
                            """
                            if type(value) != tuple:
                                raise TypeError("position must be a tuple of 2 positive integers")
                            elif len(value) != 2:
                                raise TypeError("position must be a tuple of 2 positive integers")
                            elif isinstance(value[0], int) is False:
                                raise TypeError("position must be a tuple of 2 positive integers")
                            elif isinstance(value[1], int) is False:
                                raise TypeError("position must be a tuple of 2 positive integers")
                            elif value[0] < 0 or value[1] < 0:
                                raise TypeError("position must be a tuple of 2 positive integers")
                            else:
                                self.__position = value#!/usr/bin/python3
                                """Class for Node"""
                                class Node:
                                    """ defines a node of a singly linked list
                                     Attributes:
                                     data (int): data
                                     next_node (Node, optional): node
                                     """

                                     def __init__(self, data, next_node=None):
                                         """Initialize Node
                                         args:
                                         data (int): data stored in node
                                         next_node (Node): next node
                                         """
                                         self.data = data
                                         self.next_node = next_node

                                         @property
                                         def data(self):
                                             """data getter
                                             returns:
                                             data (int)
                                             """
                                             return self.__data

                                         @data.setter
                                         def data(self, value):
                                             """data setter
                                             args:
                                             value (int): value to set
                                             returns:
                                             None
                                             """
                                             if type(value) != int:
                                                 raise TypeError("data must be an integer")
                                             self.__data = value

                                             @property
                                             def next_node(self):
                                                 """data getter
                                                 returns:
                                                 data (int)
                                                 """
                                                 return self.__next_node

                                             @next_node.setter
                                             def next_node(self, value):
                                                 """data setter
                                                 args:
                                                 value (Node): value to set
                                                 returns:
                                                 None
                                                 """
                                                 if not isinstance(value, Node) and value is not None:
                                                     raise TypeError("next_node must be a Node object")
                                                 self.__next_node = value
                                                 class SinglyLinkedList:
                                                     """Singly linked list class
                                                     """
                                                     def __init__(self):
                                                         """Initialize linked list"""
                                                         self.__head = None

                                                         def sorted_insert(self, value):
                                                             """insert node in coorect sorted position
                                                             args:
                                                             value (int): value for new node
                                                             """
                                                             new = Node(value)
                                                             if self.__head is None:
                                                                 new.next_node = None
                                                                 self.__head = new
                                                             elif self.__head.data > value:
                                                                 new.next_node = self.__head
                                                                 self.__head = new
                                                             else:
                                                                 tmp = self.__head
                                                                 while (tmp.next_node is not None and
                                                                         tmp.next_node.data < value):
                                                                     tmp = tmp.next_node

                                                                     new.next_node = tmp.next_node
                                                                     tmp.next_node = new

                                                                     def __str__(self):
                                                                         """Define the print() representation of a SinglyLinkedList."""
                                                                         values = []
                                                                         tmp = self.__head
                                                                         while tmp is not None:
                                                                             values.append(str(tmp.data))
                                                                             tmp = tmp.next_node
                                                                             return ('\n'.join(values))
