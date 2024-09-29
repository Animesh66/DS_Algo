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


"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates 
in-place such that each unique element appears only once. 
The relative order of the elements should be kept the same. 
Then return the number of unique elements in nums.
Consider the number of unique elements of nums to be k, 
to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums contain the unique elements 
in the order they were present in nums initially. 
The remaining elements of nums are not important as well as the size of nums.
Return k.
Example 2:

Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""
def find_unique_elements_list(input_list: list[int]) -> list[int]:
    uniqe_set = set()
    for element in input_list:
        if element not in input_list:
            uniqe_set.add(element)
        else:
            input_list.remove(element)
    return input_list

"""
Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
Example 1:
Input: nums = [3,4,5,2]
Output: 12 
Explanation: If you choose the indices i=1 and j=2 (indexed from 0), you will get the maximum value, that is, (nums[1]-1)*(nums[2]-1) = (4-1)*(5-1) = 3*4 = 12.
"""
def find_maximum_product(input_list: list[int]) -> int:
    # Initialize two variables to store the two largest numbers
    max1, max2 = 0, 0  # O(1), constant time initialization
 
    # Iterate through the array
    for num in input_list:  # O(n), where n is the length of the array
        # If the current number is greater than max1, update max1 and max2
        if num > max1:  # O(1), constant time comparison
            max2 = max1  # O(1), constant time assignment
            max1 = num  # O(1), constant time assignment
        # If the current number is greater than max2 but not max1, update max2
        elif num > max2:  # O(1), constant time comparison
            max2 = num  # O(1), constant time assignment
 
    # Return the product of the two largest numbers
    return max1 * max2  # O(1), constant time multiplication
 
# input_list1 = [1, 7, 3, 4, 9, 5]
# print(find_maximum_product(input_list1))

"""
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.
You can return the answer in any order.
Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
"""
def find_two_sum(input_list: list[int], target: int) -> list[int]:
    seen = {}
    for index, num in enumerate(input_list): 
         complement = target - num
         if complement in seen:
            return [seen[complement], index]
         else:
            seen[num] = index

"""
Given 2D list calculate the sum of diagonal elements.
Example
myList2D= [[1,2,3],[4,5,6],[7,8,9]] 
 
diagonal_sum(myList2D) # 15
"""
def diagonal_sum(input_list: list[int]) -> int:
    diagonal_sum = 0
    for index, element in enumerate(input_list):
        diagonal_sum += element[index]
    return diagonal_sum


# input_list = [[1,2,3],[4,5,6],[7,8,9]] 
# print(diagonal_sum(input_list))

"""
Given a list, write a function to get first, second best scores from the list.
List may contain duplicates.
Example
myList = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
first_second(myList) # 90 87
"""
def first_second(input_list: list[int]) -> int:
    non_duplicate = set(input_list)
    sorted_list = sorted(list(non_duplicate), reverse=True)
    return sorted_list[:2]

def first_and_second_without_sort(input_list: list[int]) -> int:
    first, second = 0, 0
    for number in input_list:
        if number > first:
            second = first
            first = number
        if number > second and number != first:
            second = number
    return first, second

# input_list = [84,85,86,87,85,90,90,87,85,83,23,45,84,1,2,0]
# print(first_and_second_without_sort(input_list))

"""
Write a function to remove the duplicate numbers on given integer array/list.
Example
remove_duplicates([1, 1, 2, 2, 3, 4, 5])
Output : [1, 2, 3, 4, 5]
"""
def remove_duplicates(input_list: list[int]) -> list[int]:
    output_list = []
    for item in input_list:
        if item not in output_list:
            output_list.append(item)
    return output_list

# print(remove_duplicates([1, 1, 2, 2, 3, 4, 5]))

"""
Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.
Example
pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
Output : ['2+5', '4+3', '3+4', '-2+9']
"""
def find_pairs(input_list: list[int], number: int) -> list[str]:
    output_list = []
    for index, item in enumerate(input_list):
        complement = number - item
        if complement in input_list[index + 1:]:
            output_list.append(f'{item} + {complement}')
    return output_list

# print(find_pairs([2, 4, 3, 5, 6, -2, 4, 7, 8, 9], 7))

"""
Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Example :
Input: nums = [1,2,3,1]
Output: true
"""

def contains_duplicate(input_list: list[int]) -> bool:
    for index, item in enumerate(input_list):
        if item in input_list[index + 1:]:
            return True
    return False

# print(contains_duplicate([1,2,3]))

"""
Check if two given lists are permutation of each other or not.
"""
def check_permutation(first_input_list: list[int | str], second_input_list: list[int | str]) -> bool:
    if len(first_input_list) != len(second_input_list):
        return False
    for item in first_input_list:
        if item not in second_input_list:
            return False
    return True

# print(check_permutation([1, 'a', 3], [1, 3, 'a']))
    
"""
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.
Example:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]
"""

def rotate_matrix(input_matrix: list[list[int]]) -> list[list[int]]:
    # Transpose the matrix  
    for row_number in range(len(input_matrix)): # Iterate over the rows
        for column_number in range(row_number, len(input_matrix)): # Iterate over the columns starting from the current row
            # Swap the elements at positions (row_number, column_number) and (column_number, row_number)
            input_matrix[row_number][column_number], input_matrix[column_number][row_number] = input_matrix[column_number][row_number], input_matrix[row_number][column_number]
     # Reverse each row
    for row in input_matrix:  # Iterate over each row in the matrix
        row.reverse()  # Reverse the elements in the current row
    return input_matrix

# print(rotate_matrix([[1,2,3],[4,5,6],[7,8,9]]))

"""
Define a function with takes two dictionaries as parameters and merge them and sum the values of common keys.
Example:
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}
merge_dicts(dict1, dict2)
Output: {'a': 1, 'b': 5, 'c': 7, 'd': 5}
"""

def merge_dicts(first_dict: dict, second_dict: dict) -> dict:
    merge_dict = first_dict.copy()
    for key, value in second_dict.items():
        merge_dict[key] = merge_dict.get(key, 0) + value
    return merge_dict

print(merge_dicts({'a': 1, 'b': 2, 'c': 3},{'b': 3, 'c': 4, 'd': 5}))

"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.
Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
Example 1:
Input: x = 123
Output: 321
"""

def reverse(x: int) -> int:
    # Define the 32-bit signed integer range limits
    INT_MIN, INT_MAX = -2**31, 2**31 - 1

    # Determine if the number is negative
    sign = -1 if x < 0 else 1

    # Reverse the absolute value of the integer and apply the sign
    reversed_num = int(str(abs(x))[::-1]) * sign

    # If the reversed number is out of the 32-bit signed integer range, return 0
    if reversed_num < INT_MIN or reversed_num > INT_MAX:
        return 0

    return reversed_num
