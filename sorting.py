def bubble_sort(input_list: list[int]) -> list[str]:
    """
    This method will sort the input list using bubble sort algorithm.
    time complexity for this algorithm is O(n^2) in worst case(sorted in reverse) and O(n) in bests case(list already sorted)
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


def selection_sort(input_list: list[int]) -> list[str]:
    """
    This function will sort the list using selection sort algorithm.
    We assume the first index is the minimum value and compare the elements with 
    other and swap the elements if needed.
    The time complexity for this algorithm is O(n^2) in both best case(list already sorted) and worst case(sorted in reverse).
    """
    for i in range(len(input_list)):
        min_index = i
        for j in range(i, len(input_list)):
            if input_list[j] < input_list[min_index]:
                min_index = j
        if i != min_index:  # Swap only when needed otherwise not required.
            input_list[i], input_list[min_index] = input_list[min_index], input_list[i]
    return input_list


def insertion_sort(input_list: list[str]) -> list[str]:
    """
    This function will sort the list using insertion sort algorithm.
    We loop though all the element and sort them in place instead of swaping the elements we shift elemets to wright.
    other and swap the elements if needed.
    The time complexity for this algorithm is O(n) in best case(list already sorted) and O(n^2) in worst case(sorted in reverse).
    """
    # We are starting with second element in the list assuming first element is in corect place.
    # Once we go to the 2nd element we will verify if the element is greater or not.
    for i in range(1, len(input_list)):
        # set the current element to the ith element to compare it with previous element.
        current = input_list[i]
        # in the inner loop we will compare the value of the previous element with current element.
        j = i - 1
        while (j >= 0 and current < input_list[j]):
            input_list[j + 1] = input_list[j]
            input_list[j] = current
            j -= 1

    return input_list


def merge_sort(input_list: list[int]) -> list[int]:
    """
    Merge sort use divide and conqure rule and divide the array to small arrays and then recursively
    sort them and merge the arrays.
    The time complexity of the merge sort is O(nlogn)[divide is O(log n) and merge is O(n)] 
    and space complexity is O(n) as we have to allocate extra space for the sub arrays.
    input_list = [23, 18, 55, 21, 7] 
    left_sub_list = [23, 18]
    right_sub_list = [55, 21, 7]
    """
    # Base condition for the merge sort recursion is when the list length is one and no more division possible.
    if len(input_list) == 1:
        return input_list
    # first recursively divide the list with two equal lists and untill list size gets to 1
    middle_index = len(input_list) // 2
    left_sub_list = merge_sort(input_list[:middle_index])
    right_sub_list = merge_sort(input_list[middle_index:])
    # merge the sorted list so that the resulted list is sorted.
    return merge(left_sub_list, right_sub_list)


def merge(left_sub_list: list[int], right_sub_list: list[int]) -> list[int]:
    """
    This list will merge both the left and right sub lists in sorted order
    """
    i = 0
    j = 0
    resulted_list = []
    # Loop through the two left and right sublist and then compare the values of each list
    # and append tot the resulted list in sorted order.
    while (i < len(left_sub_list) and j < len(right_sub_list)):
        if left_sub_list[i] <= right_sub_list[j]:
            resulted_list.append(left_sub_list[i])
            i += 1
        else:
            resulted_list.append(right_sub_list[j])
            j += 1
    # In case after sorting is done
    # but left list still have extra items left
    # then add it into the resulted list
    while (i < len(left_sub_list)):
        resulted_list.append(left_sub_list[i])
        i += 1
    # In case after sorting is done
    # but right list still have extra items left
    # then add it into the resulted list
    while (j < len(right_sub_list)):
        resulted_list.append(right_sub_list[j])
        j += 1
    return resulted_list


input_list = [13, 10, 8, 22, 59, 55]

print(merge_sort(input_list))
