import math

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
    The time complexity of linear search is O(log n)(base 2)
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
def ternary_search(input_list: list[int], search_item: int) -> int:
    """
    Public method to kick of the recursion for the ternary seach private method.
    """
    return _ternary_search(input_list=input_list, 
                           search_item=search_item,
                           left_index=0,
                           right_index=len(input_list) - 1)


def _ternary_search(input_list: list[int], 
                    search_item: int,
                    left_index: int,
                    right_index: int) -> int:
    """
    This function is search an element from a list using ternary search algorithm.
    In Ternary search we divide the list into 3 partitins and calculate the middle point of each 
    partition. So we will have two middle points.
    Time complexity of ternary search is O(log n)(base 3)
    Space complexity of ternary seach is O(log n) in recustion and O(1) using iteratively.
    This function is implemented using recursion.
    Binary search is faster than ternary search.
    """
    # Implement the base condition for recursion. If the left index is greater than right index.
    # thta means the searched item does not exists in the input list.
    if left_index > right_index:
        return -1
    #  Calculate the partition size and index of thow boundaries.
    partition_size = (right_index - left_index) // 3
    first_mid = left_index + partition_size
    second_mid = right_index - partition_size
    #  Check if the first mid is equals to the search item or not.
    if input_list[first_mid] == search_item:
        return first_mid
    #  Check if the second mid is equals to the search item or not.
    if input_list[second_mid] == search_item:
        return second_mid
    #  Check if the search item is less than the first mid value then search left.
    if search_item < input_list[first_mid]:
        return _ternary_search(input_list, search_item, left_index, first_mid - 1)
    #  Check if the search item is greater than the second mid value then search right.
    if search_item > input_list[second_mid]:
        return _ternary_search(input_list, search_item, second_mid + 1, right_index)
    # If none of the above condition are true then the search item is in middle partition.
    return _ternary_search(input_list, search_item, first_mid + 1, second_mid - 1)

def jump_search(input_list: list[int], search_item: int) -> int:
    """
    This function will take an input list and returns the index of the search item form the list.
    This algorithm use jump search where we divide the sorted list into different blocks and we search
    for the elements on that block only.
    Time complexity of this jump search is O(sqrt(n))
    We divide the list with sqrt(n) number of blocks.
    """
    # First calculate the block size
    block_size = int(math.sqrt(len(input_list)))
    # Take two pointers and poitn to the start index of two consecutive blocks.
    start = 0
    next = block_size
    # Loop though the items and identify the block in which the item may exists.
    while (input_list[next - 1] < search_item and start < len(input_list)):
        start = next
        next += block_size
        if next > len(input_list):
            next = len(input_list)
    # Now when we find the potential block then perform a liner search on that block to find the item.
    for i in range(start, next):
        if input_list[i] == search_item:
            return i
    return -1 

def exponential_search(input_list: list[int], search_item: int) -> int:
    """
    This function will take an input list and returns the index of the search item form the list.
    This algorithm uses exponential search where we divide the sorted list into different blocks
    first we define the block size to index 1 means the first two items and we double the block size 
    in every search. 
    """
    # Set the initial size of the block
    block_size = 1
    # Loop over the items until the block is not found
    while (block_size < len(input_list) and input_list[block_size] < search_item):
        block_size *= 2
    #  Now perform a binary search on that block
    left_index = block_size // 2
    right_index = min(block_size, len(input_list) - 1)
    return _binary_search_recursive(input_list, search_item, left_index, right_index)

input_list = [8, 10, 13, 22, 55, 63]
print(exponential_search(input_list, 58))
