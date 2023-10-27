"""
    Stack Class
""" 
class Stack():
    def __init__(self, elements=[]):
        self._stack = elements
    def __str__(self):
        return str(self._stack)

    """
        peek
        
        Returns the top object without removing it.

        :return: last pushed object
    """ 
    def peek(self):
        if len(self._stack) > 0:
            return self._stack[len(self._stack)-1]
        else:
            return None

    """
        push

        Appends the object to the top of the stack
    """ 
    def push(self, element):
        self._stack.append(element)

    """
        pop

        Removes and returns the last pushed object

        :return: popped object
    """ 
    def pop(self):
        if len(self._stack) > 0:
            return self._stack.pop()
        else:
            return None

    """
        clear 
    """ 
    def clear(self):
        while len(self._stack) > 0:
            self.pop()

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
    stack.clear()
    print(stack)

if __name__ == "__main__":
    practice_stack()
