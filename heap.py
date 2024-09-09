class MaxHeap:

    def __init__(self) -> None:
        self.heap = []

    def _left_child_index(self, index: int) -> int:
        """
        Method to provide the left child index of the given index.
        """
        return (2 * index) + 1

    def _left_child(self, index: int) -> int:
        """
        This method will return the left child of the provided index. 
        """
        return self.heap[self._left_child_index(index)]

    def _right_child(self, index: int) -> int:
        """
        This method will return the right child of the given index
        """
        return self.heap[self._right_child_index(index)]

    def _parent(self, index: int) -> int:
        """
        This method will return the parent element of the provided index
        """
        return self.heap[self._parent_index(index)]

    def _right_child_index(self, index: int) -> int:
        """
        Method to provide the right child index of the given index.
        """
        return (2 * index) + 2

    def _parent_index(self, index: int) -> int:
        """
        Method to return the parent index of the given index.
        """
        return (index - 1) // 2

    def _sawp(self, first_index: int, second_index: int) -> None:
        """
        Swap the values of the two given index int the list.
        """
        temp = self.heap[first_index]
        self.heap[first_index] = self.heap[second_index]
        self.heap[second_index] = temp

    def _is_valid_child(self, index: int) -> bool:
        """
        This will verify of the child is a valid child or not.
        """
        return self._parent(index) > self.heap[index]

    def insert(self, value: int) -> None:
        """
        Method to insert a value into the heap
        """
        # first append the value of the inserted item in the end of the list
        self.heap.append(value)
        # second take a reference of the last index of the item.
        inserted_index = len(self.heap) - 1
        # then continue to swap the items till its bigger than the paren of index reaches to parent index of 0
        while inserted_index > 0 and not self._is_valid_child(inserted_index):
            self._sawp(inserted_index, self._parent_index(inserted_index))
            inserted_index = self._parent_index(inserted_index)


heap = MaxHeap()
heap.insert(10)
heap.insert(7)
heap.insert(2)
heap.insert(17)
heap.insert(22)
heap.insert(15)
print(heap.heap)
