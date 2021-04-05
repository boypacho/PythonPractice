class MaxHeap():
    def __init__(self, elements=[]):
        self._heap = []
        for el in elements:
            self.push(el)
            
    def __str__(self):
        return str(self._heap)

    def peek(self):
        if len(self._heap) > 0:
            return self._heap[len(self._heap)-1]
        else:
            return None

    def push(self, value):
        self._heap.append(value)
        self.__trickle_up(len(self._heap)-1)

    def pop(self):
        popped = None
        if len(self._heap) > 2:
            self.__swap(0, len(self._heap)-1)
            popped = self._heap.pop()
            self.__trickle_down(0)
        elif len(self._heap) == 2:
            popped = self._heap.pop()
        return popped

    def __trickle_up(self, index):
        parent = index//2
        if index < 1:
            return
        elif self._heap[index] > self._heap[parent]:
            self.__swap(index, parent)
            self.__trickle_up(parent)

    def __trickle_down(self, index):
        left = index*2
        right = index*2+1
        largest = index

        if left < len(self._heap) and self._heap[left] > self._heap[largest]:
            largest = left
        if right < len(self._heap) and self._heap[right] > self._heap[largest]:
            largest = right
        if largest != index:
            self.__swap(index, largest)
            self.__trickle_down(largest)

    def __swap(self, i, j):
        self._heap[i], self._heap[j] = self._heap[j], self._heap[i]

def practice_max_heap():
    print("Practicing MaxHeap function calls")
    max_heap = MaxHeap([30,10,44,1])
    print(max_heap)
    max_heap.push(88)
    print(max_heap)
    print(max_heap.pop())
    print(max_heap)
    print(max_heap.peek())