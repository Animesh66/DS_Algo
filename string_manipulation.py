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


def remove_duplicates(input_string: str) -> str:
    """
    This method will remove all duplicate char from a string and re
    """
    return "".join(set(input_string.lower()))


def remove_duplicates_iterative(input_string: str) -> str:
    """
    This method will remove all duplicate char from a string and re
    """
    char_set = set()
    output_str = []
    for char in input_string:
        if char.lower() not in char_set:
            char_set.add(char)
            output_str.append(char)

    return "".join(output_str)


def find_most_repeated_char(input_str: str) -> tuple[str, int]:
    """
    This method will take input as string and returns the most frequent charactor count from that given string.
    """
    updated_input_str = input_str.lower().replace(" ", "")
    char_frequency = {}
    for char in updated_input_str:
        if char not in char_frequency.keys():
            char_frequency[char] = 1
        else:
            char_frequency[char] += 1
    char_frequency_sorted = sorted(
        list(char_frequency.items()), key=lambda char: char[1], reverse=True)
    return char_frequency_sorted[0]


def capitalize(input_str: str) -> str:
    """
    This method will capitalize each word of the given sentence. 
    """
    words = input_str.strip().split(" ")
    output_words = []
    for word in words:
        output_words.append(word.title())
    return " ".join(output_words)


print(capitalize("my name is animesh mukherjees"))
