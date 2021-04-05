"""
    Stack

    :param p1: describe about parameter p1
    :param p2: describe about parameter p2
    :param p3: describe about parameter p3
    :return: describe what it returns
""" 
class Stack():
    def __init__(self, elements=[]):
        self._stack = elements
    def __str__(self):
        return str(self._stack)
    """
        peek
        
        returns the top element without removing the top element

        :return: top element
    """ 
    def peek(self):
        if len(self._stack) > 0:
            return self._stack[len(self._stack)-1]
        else:
            return None
    """
        push

        Places the 
        :return: describe what it returns
    """ 
    def push(self, element):
        self._stack.append(element)
    """
        pop

        :return: 
    """ 
    def pop(self):
        if len(self._stack) > 0:
            return self._stack.pop()
        else:
            return None

def practice_stack():
    print("Practicing Stack function calls")
    stack = Stack()
    stack.push(1)
    stack.push("Lingo")
    print(stack)
    print(stack.pop())
    stack.push(stack.peek())
    print(stack)
    print(stack.pop())
    print(stack)
    stack.push((3,'hello world'))
    print(stack)
    stack = None
    print(stack)