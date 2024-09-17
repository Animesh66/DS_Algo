def bubble_sort(input_list: list[int]):
    """
    This method will sort the input list using bubble sort algorithm.
    time complexity for this algorithm is O(n^2)
    """
    is_sorted = True  # This is an improvement in case the array is sorted.
    for i in range(len(input_list)):
        #  In each pass if the value of the next element greater that next then swap the elements.
        for j in range(1, len(input_list) - i):
            if input_list[j] < input_list[j - 1]:
                input_list[j], input_list[j-1] = input_list[j-1], input_list[j]
                is_sorted = False
        # if the list is already sorted then we will not run the loop again.
        if is_sorted:
            return

    return input_list


def selection_sort(input_list: list[int]):
    """
    This function will sort the list using selection sort algorithm.
    We assume the first index is the minimum value and compare the elements with 
    other and swap the elements if needed.
    The time complexity for this algorithm is O(n^2)
    """
    for i in range(len(input_list)):
        min_index = i
        for j in range(i, len(input_list)):
            if input_list[j] < input_list[min_index]:
                min_index = j
        input_list[i], input_list[min_index] = input_list[min_index], input_list[i]
    return input_list


input_list = [13, 10, 8, 22, 59, 55]

print(selection_sort(input_list))
