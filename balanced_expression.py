from stack import Stack


def balanced_expression(input_expression: str) -> bool:
    stack = Stack()
    for char in input_expression:
        if char == "(" or char == "<" or char == "[" or char == "{":
            stack.push(char)
        if char == ")" or char == ">" or char == "]" or char == "}":
            if stack.is_empty():
                return False
            top = stack.pop()
            if char == ")" and top != "(":
                return False
            if char == ">" and top != "<":
                return False
            if char == "]" and top != "[":
                return False
            if char == "}" and top != "{":
                return False
    return stack.is_empty()


print(balanced_expression("(1 + 2>"))
