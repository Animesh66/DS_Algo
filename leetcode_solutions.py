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


from collections import defaultdict


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
    for row_number in range(len(input_matrix)):  # Iterate over the rows
        # Iterate over the columns starting from the current row
        for column_number in range(row_number, len(input_matrix)):
            # Swap the elements at positions (row_number, column_number) and (column_number, row_number)
            input_matrix[row_number][column_number], input_matrix[column_number][
                row_number] = input_matrix[column_number][row_number], input_matrix[row_number][column_number]
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

# print(merge_dicts({'a': 1, 'b': 2, 'c': 3},{'b': 3, 'c': 4, 'd': 5}))


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


"""
Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.
Example:
my_dict = {'a': 5, 'b': 9, 'c': 2}
max_value_key(my_dict))
Output: b
"""


def max_value_key(input_dict: dict) -> str:
    sorted_list = sorted(input_dict.items(),
                         key=lambda item: item[1], reverse=True)
    return sorted_list[0][0]

# print(max_value_key({'a': 5, 'b': 9, 'c': 2}))


"""
Define a function which takes as a parameter dictionary and returns a dictionary in which reverse the key-value pairs are reversed.
Example:
my_dict = {'a': 1, 'b': 2, 'c': 3}
reverse_dict(my_dict)
Output: {1: 'a', 2: 'b', 3: 'c'}
"""


def reverse_dict(my_dict: dict) -> dict:
    reverse_dict = {}
    for key, value in my_dict.items():
        reverse_dict[value] = key
    return reverse_dict

# print(reverse_dict({'a': 1, 'b': 2, 'c': 3}))


"""
Define a function that takes a dictionary as a parameter and returns a dictionary with elements based on a condition.
Example:
my_dict = {'a': 1, 'b': 2, 'c': 3, 'd': 4} 
filtered_dict = filter_dict(my_dict, lambda k, v: v % 2 == 0) 
Output:
{'b': 2, 'd': 4}
"""


def filter_dict(my_dict, condition):
    return {k: v for k, v in my_dict.items() if condition(k, v)}


"""
Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.
Example:
list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]
check_same_frequency(list1, list2)
Output: False
"""


def check_same_frequency(list1, list2):
    def count_elements(lst):
        counter = {}
        for element in lst:
            counter[element] = counter.get(element, 0) + 1
        return counter

    return count_elements(list1) == count_elements(list2)


"""
Write a function that calculates the sum and product of all elements in a tuple of numbers.
Example
input_tuple = (1, 2, 3, 4)
sum_result, product_result = sum_product(input_tuple)
print(sum_result, product_result)  # Expected output: 10, 24
"""


def calculate_sum_and_product(input_tuple: tuple[int]) -> tuple[int]:
    sum = 0
    product = 1
    for element in input_tuple:
        sum += element
        product *= element
    return (sum, product)

# print(calculate_sum_and_product((1, 2, 3, 4)))


"""
Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.
Example
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
output_tuple = tuple_elementwise_sum(tuple1, tuple2)
print(output_tuple)  # Expected output: (5, 7, 9)
"""


def tuple_elementwise_sum(first_tuple: tuple[int], second_tuple: tuple[int]):
    combined = list(zip(first_tuple, second_tuple))
    output_list = []
    for items in combined:
        output_list.append(items[0] + items[1])
    return tuple(output_list)

# print(tuple_elementwise_sum((1, 2, 3), (4, 5, 6)))


"""
Write a function that takes a tuple and a value, and returns a new tuple with the value inserted at the beginning of the original tuple.
Example
input_tuple = (2, 3, 4)
value_to_insert = 1
output_tuple = insert_value_front(input_tuple, value_to_insert)
print(output_tuple)  # Expected output: (1, 2, 3, 4)
"""


def insert_value_front(input_tuple: tuple[int], value_to_insert: int):
    return (value_to_insert,) + input_tuple


"""
Write a function that takes a tuple of strings and concatenates them, separating each string with a space.
Example
input_tuple = ('Hello', 'World', 'from', 'Python')
output_string = concatenate_strings(input_tuple)
print(output_string)  # Expected output: 'Hello World from Python'
"""


def concatenate_strings(input_tuple):
    return " ".join(input_tuple)

# print(concatenate_strings(('Hello', 'World', 'from', 'Python')))


"""
Create a function that takes a tuple of tuples and returns a tuple containing the diagonal elements of the input.
Example
input_tuple = ((1, 2, 3),(4, 5, 6),(7, 8, 9))
output_tuple = get_diagonal(input_tuple)
print(output_tuple)  # Expected output: (1, 5, 9)
"""


def get_diagonal(input_tuple):
    return tuple(input_tuple[i][i] for i in range(len(input_tuple)))

# print(get_diagonal(((1, 2, 3),(4, 5, 6),(7, 8, 9))))


"""
Write a function that takes two tuples and returns a tuple containing the common elements of the input tuples.
Example
tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
output_tuple = common_elements(tuple1, tuple2)
print(output_tuple)  # Expected output: (4, 5)
"""


def common_elements(tuple1, tuple2):
    return tuple(item for item in tuple1 if item in tuple2)

# print(common_elements((1, 2, 3, 4, 5),(4, 5, 6, 7, 8)))


"""
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""


"""
You are given the heads of two sorted linked lists list1 and list2. 
Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.
Return the head of the merged linked list.   
Example 1: 
Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:
Input: list1 = [], list2 = []
Output: []
"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prehead = ListNode(-1)

        prev = prehead
        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        # At least one of l1 and l2 can still have nodes at this point, so connect
        # the non-null list to the end of the merged list.
        prev.next = l1 if l1 is not None else l2

        return prehead.next


"""
Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well. 
Example 1:
Input: head = [1,1,2]
Output: [1,2]
Example 2:
Input: head = [1,1,2,3,3]
Output: [1,2,3]
"""


class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        if not head:
            return None

        seen = set()
        dummy = ListNode(-1)
        dummy.next = head
        prev_node = dummy
        current_node = head

        while current_node:
            if current_node.val in seen:
                prev_node.next = current_node.next
                current_node = current_node.next
            else:
                seen.add(current_node.val)
                prev_node = current_node
                current_node = current_node.next

        return dummy.next


"""
Given a string s, find the length of the longest 
substring without repeating characters.
Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.
Example 2:
Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.
Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

"""


def length_of_longest_substring(s: str) -> int:
    # Dictionary to store the last index of each character
    char_index_map = {}
    # Initialize the start pointer and the max length of the substring
    start = 0
    max_length = 0

    # Loop through the string using an index i
    for i, char in enumerate(s):
        # If the character is found in the map and is part of the current window
        if char in char_index_map and char_index_map[char] >= start:
            # Move the start pointer to the right of the last occurrence of the current character
            start = char_index_map[char] + 1
        # Update the last seen index of the character
        char_index_map[char] = i
        # Update the max length of the substring
        max_length = max(max_length, i - start + 1)

    return max_length


"""
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
For example, 2 is written as II in Roman numeral, just two ones added together. 
12 is written as XII, which is simply X + II. 
The number 27 is written as XXVII, which is XX + V + II.
Roman numerals are usually written largest to smallest from left to right. 
However, the numeral for four is not IIII. Instead, the number four is written as IV. 
Because the one is before the five we subtract it making four. 
The same principle applies to the number nine, which is written as IX. 
There are six instances where subtraction is used:
I can be placed before V (5) and X (10) to make 4 and 9. 
X can be placed before L (50) and C (100) to make 40 and 90. 
C can be placed before D (500) and M (1000) to make 400 and 900.
Given a roman numeral, convert it to an integer.
Example 1:
Input: s = "III"
Output: 3
Explanation: III = 3. 
"""


def roman_to_interger(roman: str) -> int:
    map_converter = {'I': 1, 'V': 5, 'X': 10,
                     'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    # Initialize the total to 0 and the previous value to 0
    total = 0
    prev_value = 0
    if roman in map_converter.keys():
        return map_converter[roman]
    # Traversed the list from right to left.
    for char in reversed(roman):
        current_value = map_converter[char]
        #  If the current value is less than the previous value, subtract it
        if current_value < prev_value:
            total -= current_value
        else:
            # Otherwise, add the current value
            total += current_value
        # Update the previous value
        prev_value = current_value
    return total


# print(roman_to_interger('XII'))

"""
Write a method to convert from decimal to binary number.
"""


def decimal_to_binary(decimal: int) -> int:
    # provide a base condition for recursion.
    if decimal == 0:
        return decimal
    else:
        # Otherwise calculate the binary using formula (reminder + 10 * quicent)
        return decimal % 2 + 10 * decimal_to_binary(int(decimal/2))


# print(decimal_to_binary(12))

"""
Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
An input string is valid if:
Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.
Every close bracket has a corresponding open bracket of the same type.
Example 1:
Input: s = "()"
Output: true
Example 2:
Input: s = "()[]{}"
Output: true
Example 3:
Input: s = "(]"
Output: false
Example 4:
Input: s = "([])"
Output: true
"""


def check_opening_closing_brackets(input_str: str) -> bool:
    # Create a stack to store the opening brackets.

    opening_brackets = ["(", "{", "["]
    closing_brackets = [")", "}", "]"]
    bracket_stack = []
    # Loop over the items to go over the brackets.
    for item in input_str:
        if item in opening_brackets:
            bracket_stack.append(item)
        if item in closing_brackets:
            if len(bracket_stack) == 0:
                return False
            top = bracket_stack[len(bracket_stack) - 1]
            if item == ")" and top == "(":
                bracket_stack.pop()
            if item == "}" and top == "{":
                bracket_stack.pop()
            if item == "]" and top == "[":
                bracket_stack.pop()
    return len(bracket_stack) == 0


# print(check_opening_closing_brackets(input_str="(]"))

"""
Given an array of integers arr of even length n and an integer k.
We want to divide the array into exactly n / 2 pairs 
such that the sum of each pair is divisible by k.
Return true If you can find a way to do that or false otherwise.
Example 1:
Input: arr = [1,2,3,4,5,10,6,7,8,9], k = 5
Output: true
Explanation: Pairs are (1,9),(2,8),(3,7),(4,6) and (5,10).
Example 2:
Input: arr = [1,2,3,4,5,6], k = 7
Output: true
Explanation: Pairs are (1,6),(2,5) and(3,4).
Example 3:
Input: arr = [1,2,3,4,5,6], k = 10
Output: false
Explanation: You can try all possible pairs to see that there is no way to divide arr into 3 pairs each with sum divisible by 10.
"""


def find_divisible_pairs(input_list: list[int], k: int) -> bool:
    # Create a dictionary to store frequencies of remainders
    remainder_count = defaultdict(int)

    # Count frequencies of the remainder when elements are divided by k
    for num in input_list:
        remainder = num % k
        remainder_count[remainder] += 1

    # Iterate through the unique remainders
    for rem in remainder_count:
        # Special case: if the remainder is 0, the count of these numbers must be even
        if rem == 0:
            if remainder_count[rem] % 2 != 0:
                return False
        # Special case: if remainder is exactly half of k (only possible when k is even),
        # we also need an even number of such elements
        elif rem * 2 == k:
            if remainder_count[rem] % 2 != 0:
                return False
        # For all other cases, check if remainder_count[rem] == remainder_count[k - rem]
        else:
            if remainder_count[rem] != remainder_count[k - rem]:
                return False

    return True


"""
Write a function to find the longest common prefix string amongst an array of strings.
If there is no common prefix, return an empty string "".
Example 1:
Input: strs = ["flower","flow","flight"]
Output: "fl"
Example 2:
Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.
"""


def longest_common_prefix(input_list: list[str]):
    if not input_list:
        return ""
    # Start with the first word as the prefix
    prefix = input_list[0]
    # Start with the next words except the first.
    for string in input_list[1:]:
        # Reduce the prefix until it matches the start of the current string
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""

    return prefix


"""
Given an integer array nums and an integer val, 
remove all occurrences of val in nums in-place. 
The order of the elements may be changed. 
Then return the number of elements in nums which are not equal to val.
Consider the number of elements in nums which are not equal to val be k, 
to get accepted, you need to do the following things:
Change the array nums such that the first k elements of nums 
contain the elements which are not equal to val. 
The remaining elements of nums are not important as well as the size of nums.
Return k.
Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]
Explanation: Your function should return k = 2, with the first two elements of nums being 2.
It does not matter what you leave beyond the returned k (hence they are underscores).
Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]
Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
Note that the five elements can be returned in any order.
It does not matter what you leave beyond the returned k (hence they are underscores).
"""


def remove_all_occurance_of_k(input_list: list[int], k: int) -> list[int]:
    return [item for item in input_list if item != k], len([item for item in input_list if item != k])


# print(remove_all_occurance_of_k([0, 1, 2, 2, 3, 0, 4, 2], 2))

"""
Given two strings needle and haystack, 
return the index of the first occurrence of needle in haystack, 
or -1 if needle is not part of haystack.
Example 1:
Input: haystack = "sadbutsad", needle = "sad"
Output: 0
Explanation: "sad" occurs at index 0 and 6.
The first occurrence is at index 0, so we return 0.
Example 2:
Input: haystack = "leetcode", needle = "leeto"
Output: -1
Explanation: "leeto" did not occur in "leetcode", so we return -1.
"""


def match_index_of_two_string(needle: str, haystack: str) -> int:
    return haystack.find(needle)


print(match_index_of_two_string("leeto", "leetcode"))

"""
Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
"""


def find_insert_index_of_k(input_list: list[int], taget: int) -> int:
    # In order to make it a O(logn) so use binary search instead of liner search.
    left, right = 0, len(input_list) - 1
    while left <= right:
        mid = (left + right) // 2  # Find the middle index
        if input_list[mid] == taget:
            return mid  # Target found, return its index
        elif input_list[mid] < taget:
            left = mid + 1  # Move the search to the right half
        else:
            right = mid - 1  # Move the search to the left half

    return left  # If not found, return the index where it should be inserted
