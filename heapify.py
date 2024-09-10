from heap import MaxHeap


class Heapfy:

    @classmethod
    def heapify(cls, input_list: list[int]) -> list[int]:
        """
        Method to heapify an provided list.
        """
        last_parent_index = len(input_list) // 2 - 1
        for index in range(last_parent_index, -1, -1):
            cls.__heapify(input_list, index)
        return input_list

    @classmethod
    def __heapify(cls, input_list: list[int], index: int) -> None:
        """
        helper method to perform recursion for heapify.
        """
        # Assume that the root index is larger index
        larger_index = index
        # Calculate the values of left and right child index.
        # verify if the left child index value is greater than the larger index value
        # and left child index is a valid index
        left_child_index = index * 2 + 1
        if (left_child_index < len(input_list)) and (input_list[left_child_index] > input_list[larger_index]):
            larger_index = left_child_index
        # verify if the right child index value is greater than the larger index value
        # and right child index is a valid index
        right_child_index = index * 2 + 2
        if (right_child_index < len(input_list)) and (input_list[right_child_index] > input_list[larger_index]):
            larger_index = right_child_index
        # if the item in the index is greater than both of the left and right child
        # then the item is in correct position so return.
        # This is the base condition of the recursion.
        if (index == larger_index):
            return
        # Now swap the value of the list with larger item\
        cls.__swap(index, larger_index, input_list)
        cls.__heapify(input_list, larger_index)

    @classmethod
    def __swap(cls, first: int, second: int, input_list: list[int]):
        """
        This method swaps the values of the items.
        """
        input_list[first], input_list[second] = input_list[second], input_list[first]

    @classmethod
    def get_kth_largest_element(cls, input_list: list[int], k: int) -> int:
        """
        Method to find the kth larget element from a list of integers.
        """
        heap = MaxHeap()
        # Verify k is a valid number between 1 and the length of the input_list
        if k < 1 or k > len(input_list):
            raise IndexError("value of k is not valid.")
        #  First put all the elements of the list in a heap.
        for item in input_list:
            heap.insert(item)
        # Use a for loop to remove the elemnt from heap till the kth largest becomes the root.
        for _ in range(1, k):
            heap.remove()
        # The root element is now the kth largest element.
        return heap.max_value()


convert_heap = [3, 5, 8, 6, 2, 7]
print(Heapfy.get_kth_largest_element(convert_heap, k=7))
