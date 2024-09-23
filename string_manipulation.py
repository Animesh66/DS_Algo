def count_vowels(input_string: str) -> int:
    """
    This method will take a input string and returns the count of the vowels on that string.
    """
    if not input_string:
        return 0
    vowels = "aeiou"
    count = 0
    for char in input_string:
        if char.lower() in vowels:
            count += 1
    return count


def string_reverse(input_str: str) -> str | None:
    """
    This method will take an input string as an input and output the reverse of that string. 
    """
    if input_str:
        return input_str[::-1]
    return None


def word_reverse(input_sentence: str) -> str:
    """
    This method will take input an sentence and outputs the reverse of the sentence.
    """
    if input_sentence:
        # First trim the sentence to remove any leading or lagging space then split the sentence.
        words = input_sentence.strip().split(" ")
        reverse_words = " ".join(words[::-1])
        return reverse_words
    return None


def rotation_string(first_string: str, second_string: str) -> bool:
    """
    This method will find if one string is the rotation of other string or not.
    e.g. "ABCD" is rotation of "DABC", "CDAB"
    """
    #  First check if both string have same length or not.
    if len(first_string) != len(second_string):
        return False
    #  Check if both the secpmd string is present on first string or not.
    if second_string in (first_string + first_string):
        return True
    return False


print(rotation_string("AB", "BAAB"))
