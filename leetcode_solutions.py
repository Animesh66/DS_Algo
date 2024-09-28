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
 
input_list1 = [1, 7, 3, 4, 9, 5]
print(find_maximum_product(input_list1))

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


input_list = [2,7,11,15]
print(find_two_sum(input_list, 9))
