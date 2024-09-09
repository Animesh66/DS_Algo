class Heapfy:

    def heapify(self, input_list: list[int]) -> list[int]:
        """
        Method to heapify an provided list.
        """
        for index, value in enumerate(input_list):
            self.__heapify(input_list, index)

    def __heapify(self, input_list: list[int], index: int) -> list[int]:
        """
        helper method to perfrom recursion for heapify.
        """
        # Assume that the root index is larger index
        larger_index = index
        #  calculate the values of left and right child index.
        left_child_index = index * 2 + 1
        right_child_index = index * 2 + 2
        # verify if the left child index value is greater than the larger index value
        # and left child index is a valid index
        if left_child_index < len(input_list) and input_list[left_child_index] > input_list[larger_index]:
            larger_index = left_child_index
        # verify if the right child index value is greater than the larger index value
        # and right child index is a valid index
        if right_child_index < len(input_list) and input_list[right_child_index] > input_list[larger_index]:
            larger_index = right_child_index
        # if the index is equals to the larger index that means its in correct place. hen do nothing
        if index == larger_index:
            return
        # Now swap the value of the list with larger item\
        self.__swap(index, larger_index, input_list)
        self.__heapify(input_list, larger_index)

    def __swap(self, first: int, second: int, input_list: int):
        """
        This method swaps the values of the items.
        """
        input_list[first], input_list[second] = input_list[second], input_list[first]
