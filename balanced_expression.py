from stack import Stack


def balanced_expression(input_expression: str) -> bool:
    stack = Stack()
    for char in input_expression:
        # check if its an opening bracket then push it in the stack
        if char == "(" or char == "<" or char == "[" or char == "{":
            stack.push(char)
        # if the bracket is a closing brack then we need to pop the top item
        if char == ")" or char == ">" or char == "]" or char == "}":
            #  if the char is a closing bracket and stack is empty then not blanced
            if stack.is_empty():
                return False
            top = stack.pop()
        # check if the current char is closing bracket and top is not opening bracket then not balanced
            if char == ")" and top != "(":
                return False
            if char == ">" and top != "<":
                return False
            if char == "]" and top != "[":
                return False
            if char == "}" and top != "{":
                return False
    # retrun true if the stack is empty after this operation otherwise return false
    return stack.is_empty()


print(balanced_expression("(1 + 2>"))
