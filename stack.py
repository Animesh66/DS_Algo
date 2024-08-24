class _Node:

    def __init__(self, value) -> None:
        self.value: int | str = value
        self.next = None


class Stack(_Node):

    def __init__(self) -> None:
        self.top = None
        self.length = 0

    def print_stack(self):
        current = self.top
        while current:
            print(current.value)
            current = current.next

    def push(self, value) -> bool:
        new_node = _Node(value=value)
        # case 1: check if the stack is empty
        if self.top is None:
            self.top = new_node
        # case 2: if there are at least one or more items in the stack
        else:
            new_node.next = self.top
            self.top = new_node
        self.length += 1
        return True

    def pop(self) -> _Node | None:
        # case 1: check if the stack is empty or not
        if self.top is None:
            return None
        # if there are one or more item in the stack
        else:
            current = self.top
            self.top = current.next
            current.next = None
        self.length -= 1
        return current.value

    def peek(self) -> _Node | None:
        # case 1: check if the stack is empty
        if self.top is None:
            return None
        else:
            return self.top

    def is_empty(self) -> bool:
        return self.length == 0


stack = Stack()
stack.push("a")
stack.push("b")
stack.push("c")
print(stack.is_empty())
