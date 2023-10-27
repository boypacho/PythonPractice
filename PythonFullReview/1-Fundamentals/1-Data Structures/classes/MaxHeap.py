class MaxHeap():
    def __init__(self, elements=[]):
        self._heap = []
        for el in elements:
            self.push(el)
            
    def __str__(self):
        return str(self._heap)

    def peek(self):
        if len(self._heap) > 0:
            return self._heap[0]
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
    
    def clear(self):
        self.__init__()
        return self._heap

    def __trickle_up(self, index):
        if index < 1:
            return
        parentIdx = index//2
        if self._heap[index] > self._heap[parentIdx]:
            self.__swap(index, parentIdx)
            self.__trickle_up(parentIdx)

    def __trickle_down(self, index):
        leftIdx = index*2
        rightIdx = index*2+1
        largestIdx = index

        if leftIdx < len(self._heap) and self._heap[leftIdx] > self._heap[largestIdx]:
            largestIdx = leftIdx
        if rightIdx < len(self._heap) and self._heap[rightIdx] > self._heap[largestIdx]:
            largestIdx = rightIdx
        if largestIdx != index:
            self.__swap(index, largestIdx)
            self.__trickle_down(largestIdx)

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
    print(max_heap.pop())
    print(max_heap.pop())
    print(max_heap)
    print(max_heap.peek())
    max_heap.push(5)
    max_heap.push(15)
    max_heap.push(0)
    print(max_heap)
    print(max_heap.pop())
    print(max_heap)
    print(max_heap.pop())
    print(max_heap)
    print(max_heap.peek())
    print(max_heap)
    print(max_heap.clear())

if __name__ == "__main__":
    practice_max_heap()