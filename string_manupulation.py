def count_vowels(input_string: str):
    vowels = "aeiou"
    count = 0
    for char in input_string:
        if char.lower() in vowels:
            count += 1
    return count


print(count_vowels("My name is Animeh Muherjee"))
