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
def missing_number(arr, n):
    pass


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


print(find_first_repeated_char("I am a very good boy"))
