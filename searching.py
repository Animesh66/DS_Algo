def liner_search(input_list: list[int], item: int) -> int:
    """
    This function illustrates the liner search algorithm.
    This method takes an list and the rquired item to search and return the index of the search item.
    in case the element does not exists then it returns -1
    """
    for index, element in enumerate(input_list):
        if item == element:
            return index
    return -1


input_list = [13, 10, 8, 22, 59, 55]
print(liner_search(input_list, 50))
