from stack import Stack


def string_reverser(input_str: str) -> str:
    stck = Stack()
    reversed = ""
    for char in input_str:
        stck.push(char)
    while not stck.is_empty():
        reversed += stck.pop()
    return reversed


result = string_reverser("animal")
print(result)
