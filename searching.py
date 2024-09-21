def liner_search(input_list: list[int], item: int) -> int:
    """
    This function illustrates the liner search algorithm.
    This method takes an list and the required item to search and return the index of the search item.
    In case the element does not exists then it returns -1
    time complexity of liner search is O(n)
    """
    for index, element in enumerate(input_list):
        if item == element:
            return index
    return -1

def binary_search(input_list: list[int], search_item: int) -> int:
    """
    Public method to call from outside
    """
    return _binary_search_recursive(input_list, 
                                    search_item=search_item, 
                                    left_index=0, 
                                    right_index=len(input_list) - 1)

def _binary_search_recursive(input_list: list[int], 
                            search_item: int,
                            left_index: int,
                            right_index: int) -> int:
    """
    This function illustrates the binary search algorithm.
    Binary search only works for sorted list.
    This method takes an list and the required item to search and return the index of the search item.
    In case the element does not exists then it returns -1
    Time complexity of liner search is O(log n)
    Space complexity for this algorithm is O(log n) in case we implement using
    recusion and O(1) if we are using iteratively.
    """
    # Implement the base condition where right index become smaller than left index.
    # That means the item is not present in the list
    if right_index < left_index:
        return -1
    # Calculate the middle index of the list.
    middle_index = (left_index + right_index) // 2
    # Verify if the search item is present on the middle index or not.
    if search_item == input_list[middle_index]:
        return middle_index
    # Check if the search item is less than middle index then search on the left half of the list.
    if search_item < input_list[middle_index]:
        return _binary_search_recursive(input_list, search_item, left_index, middle_index - 1)
    # If the search item is greater than the middle item of the list then search the right half of the list.
    return _binary_search_recursive(input_list, search_item, middle_index + 1, right_index)

def binary_search_iterative(input_list: list[int], search_item: int) -> int:
    """
    This function illustrates the binary search algorithm.
    Binary search only works for sorted lists.
    This method takes a list and the required item to search and return the index of the search item.
    In case the element does not exist then it returns -1
    The time complexity of linear search is O(log n)
    Space complexity for this algorithm is O(log n) in case we implement using
    recusion and O(1) if we are using iteration.
    """
    # Set the value of inital value left index and right index.
    left_index = 0
    right_index = len(input_list) - 1
    # Iterate through the list until left index becomes less than right index(loop though all items).
    while (left_index <= right_index):
        # Calculate the middle index from left and right index.
        middle_index = (right_index + left_index) // 2
        # Check if the middle item is the search item or not.
        if search_item == input_list[middle_index]:
            return middle_index
        # Check if the search item is less than the middle item then search left half of the list.
        elif search_item < input_list[middle_index]:
            right_index = middle_index - 1
        # Check if the search item is greater than the middle item then seach right half of the list.
        else:
            left_index = middle_index + 1
    #  If the search element is not present in the list return -1
    return -1


input_list = [8, 10, 13, 22, 55, 63]
print(binary_search_iterative(input_list, 58))
