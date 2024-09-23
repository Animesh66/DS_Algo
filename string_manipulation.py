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
    words = input_sentence.split(" ")
    reverse_words = " ".join(words[::-1])
    return reverse_words


print(word_reverse("My name is Animesh"))
