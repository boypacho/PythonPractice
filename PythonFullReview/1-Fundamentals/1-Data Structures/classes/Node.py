class Node():
    def __init__(self, _value, _next_node=None, _prev_node=None):
        self.value = _value
        self.next_node = _next_node
        self.prev_node = _prev_node
            
    def __str__(self):
        return str('('+str(self.value)+')')
