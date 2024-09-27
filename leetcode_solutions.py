"""
Missing Number
Write a function to find the missing number
in a given integer array of 1 to 100.
The function takes two parameter
the array and the number of elements
that needs to be in array.
For example if we want to find missing number
from 1 to 6 the second parameter will be 6.
Example
missing_number([1, 2, 3, 4, 6], 6) # 5
"""


def missing_number(input_list: list[int], n: int):
    # Calculate the sum of first n natural numbers
    total = n * (n + 1) // 2
    # Calculate the sum of numbers in the array
    sum_of_input_list = sum(input_list)
    # Find the missing number by subtracting sum_arr from total
    missing_number = total - sum_of_input_list

    return missing_number


"""
Find first repeated and non repeated character of a given string.
"""


def find_first_non_repeated_char(input_str: str) -> str:
    char_dict = {}
    for char in input_str.replace(" ", ""):
        if char not in char_dict:
            char_dict[char.lower()] = 1
        else:
            char_dict[char.lower()] += 1
    for char, frequency in char_dict.items():
        if frequency == 1:
            return char
    return None


def find_first_repeated_char(input_str: str) -> str:
    char_dict = {}
    for char in input_str.replace(" ", ""):
        if char not in char_dict:
            char_dict[char.lower()] = 1
        else:
            char_dict[char.lower()] += 1
    for char, frequency in char_dict.items():
        if frequency > 1:
            return char
    return None


"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
"""


def rotate_list_kth_element_from_last(input_list: list[int], k: int) -> list[int]:
    if k <= 0 or k > len(input_list):
        return input_list
    for i in range(k):
        input_list.insert(0, input_list.pop())
    return input_list


"""
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
There is only one repeated number in nums, return this repeated number.
You must solve the problem without modifying the array nums and using only constant extra space.
Example 1:
Input: nums = [1,3,4,2,2]
Output: 2
"""


def find_duplicate(input_list: list[int]) -> int:
    n = len(input_list)  # Calculate the lenth of the list
    total_sum = (n - 1) * n // 2
    # Get the total number of sum using the formula using n * (n + 1)) // 2
    input_list_sum = sum(input_list)
    duplicate_value = input_list_sum - total_sum
    return duplicate_value


input_list = [1, 3, 4, 2, 2]
print(find_duplicate(input_list))
