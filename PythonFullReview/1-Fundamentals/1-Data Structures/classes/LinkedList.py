from .Node import Node

class LinkedList():
    def __init__(self, _root=None):
        self.root = _root
        self.size = 0
    
    def __str__(self):
        node = self.root
        output_string = "["

        while node is not None:
            if node.next_node is None:
                output_string += str(node.value)
            else:
                output_string += str(node.value) + '->'
                
            node = node.next_node
        output_string += "]"

        return output_string

    def add(self, _value):
        new_node = Node(_value)
        new_node.next_node = self.root
        # Set new root
        self.root = new_node
        # Increment Size
        self.size += 1

    def find(self, _value):
        cursor = self.root
        while cursor is not None:
            if cursor.value == _value:
                return cursor
            cursor = cursor.next_node

    def remove(self, _value):
        node = self.root
        prev_node = None
        while node is not None:
            if node.value == _value:
                if prev_node is not None:
                    prev_node.next_node = node.next_node
                else:
                    self.root = node.next_node
                self.size -= 1
                return
            prev_node = node
            node = node.next_node

def practice_linked_list():
    print("Practicing LinkedList function calls")
    linked_list = LinkedList()
    print(linked_list.size, linked_list)
    linked_list.add(8)
    print(linked_list.size, linked_list)
    linked_list.add(2)
    print(linked_list.size, linked_list)
    linked_list.add(4)
    print(linked_list.size, linked_list)
    linked_list.add(10)
    print(linked_list.size, linked_list)
    linked_list.add(10)
    print(linked_list.size, linked_list)
    linked_list.add(9)
    print(linked_list.size, linked_list)
    print(linked_list.find(9))
    linked_list.remove(10)
    print(linked_list.size, linked_list)