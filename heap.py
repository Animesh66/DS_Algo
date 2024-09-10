class MaxHeap:

    def __init__(self) -> None:
        self.heap = []

    def _left_child_index(self, index: int) -> int:
        """
        Method to provide the left child index of the given index.
        """
        return (2 * index) + 1

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

    def _has_left_child(self, index: int) -> bool:
        """
        Helper method to verify if a parent have left child.
        """
        return self._left_child_index(index) < len(self.heap)

    def _has_right_child(self, index: int) -> bool:
        """
        Helper method to verify if the parent have right child.
        """
        return self._right_child_index(index) < len(self.heap)

    def _swap(self, first_index: int, second_index: int) -> None:
        """
        Swap the values of the two given index int the list.
        """
        self.heap[first_index], self.heap[second_index] = self.heap[second_index], self.heap[first_index]

    def _is_valid_child(self, index: int) -> bool:
        """
        This method will verify if the child is a valid child or not.
        """
        child = self.heap[index]
        parent = self._parent(index)
        return parent >= child

    def _is_valid_parent(self, index: int) -> bool:
        """
        This method will verify if the parent is a valid parent or not.
        """
        parent = self.heap[index]
        # case 1: if the parent does not have left child then its a valid parent
        if not self._has_left_child(index):
            return True
        # case 2: if the parent does not have a right child. Then verify that
        # the left child is less than the parent
        if not self._has_right_child(index):
            return parent >= self._left_child(index)
        left_child = self._left_child(index)
        right_child = self._right_child(index)
        # case 3: In case the parent have both left and right child. Then verify both
        return parent >= left_child and parent >= right_child

    def _larger_child_index(self, index: int) -> int:
        """
        This method will return the larger child index among two child
        """
        # case 1: verify that if the index have any left child or not.
        # If there are no left child  present(leaf node) then the larger index is parent index
        if not self._has_left_child(index):
            return index
        # case 2: verify if the index have any right child index or not.
        # If there are no right child then left child index is the larger index
        if not self._has_right_child(index):
            return self._left_child_index(index)
        larger_child_index = self._left_child_index(index) \
            if self._left_child(index) > self._right_child(index) \
            else self._right_child_index(index)
        return larger_child_index

    def _bubbling_up(self) -> None:
        """
        Helper method to bubbling the value up.
        """
        inserted_index = len(self.heap) - 1
        # then continue to swap the items till its bigger than the paren of
        # index reaches to parent index of 0
        # This method of swaping the biggher value to top is know
        # as bubbling up the item
        while inserted_index > 0 and not self._is_valid_child(inserted_index):
            self._swap(inserted_index, self._parent_index(inserted_index))
            inserted_index = self._parent_index(inserted_index)

    def _bubbling_down(self, index: int) -> None:
        """
        Helper method to bubble down the root element to correct position so that 
        the heap is still a valid heap
        """
        while (index < len(self.heap) and not self._is_valid_parent(index)):
            larger_child_index = self._larger_child_index(index)
            self._swap(index, larger_child_index)
            index = larger_child_index

    def insert(self, value: int) -> None:
        """
        Method to insert a value into the heap
        """
        # first append the value of the inserted item at the end of the list
        self.heap.append(value)
        # bubbling up the item if the heap is not a valid heap
        self._bubbling_up()

    def remove(self) -> int:
        """
        This methd will remove the root of the binary tree 
        Returns:
            int: the root of the tree which gets removed from the tree
        """
        # case 1: When the heap is empty
        if len(self.heap) == 0:
            return None
        # case 2: when there are only one item in the heap then return that item
        if len(self.heap) == 1:
            return self.heap.pop()
        # case 3: if there are more than one item in the heap.
        # copy the value of root element in a variable
        root = self.heap[0]
        # set the last element of the heap to the root element to make sure the tree is complete.
        self.heap[0] = self.heap.pop()
        # now bubble down the root element to place it in the correct position of the heap.
        index = 0
        self._bubbling_down(index)
        # return the removed element from the method
        return root

    def is_empty(self) -> bool:
        """
        Helper method to return the true if the heap is empty
        """
        return len(self.heap) == 0

    def max_value(self) -> int:
        """
        This method will return the max value of the heap.
        """
        return self.heap[0]


# heap = MaxHeap()
# heap.insert(10)
# heap.insert(7)
# heap.insert(2)
# heap.insert(17)
# heap.insert(22)
# heap.insert(15)
# print(heap.remove())
# print(heap.remove())
# print(heap.is_empty())
# print(heap.heap)
