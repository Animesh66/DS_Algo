class _Node:
    def __init__(self, item) -> None:
        self.item = item
        self.next = None


class LinkedList(_Node):
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.count = 0

    def print_list(self):
        current = self.head
        while (current):
            print(current.item)
            current = current.next

    def append(self, item):
        """
        Method for adding element at the end of link list
        Args:
            item :Any : item to be added
        """
        new_node = _Node(item)
        # if the node is first item
        if self.head is None:
            self.head = self.tail = new_node
        # if there are already items in the link list
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.count += 1
        return True

    def pop(self):
        """
        Method for removing element at the end of link list
        """
        # case 1: if there are no items in the link list
        if self.head is None:
            return None
        # case 2: if there are more than one item in the link list
        current = previous = self.head
        while current.next:
            previous = current
            current = current.next
        self.tail = previous
        self.tail.next = None
        self.count -= 1
        # case 3: if there are only one item in the link list
        if self.count == 0:
            self.head = self.tail = None
        return current

    def prepend(self, item):
        """
        Method for adding an element at the begining of the list
        Args:
            item (int): the value to be put node
        """
        new_node = _Node(item)
        # case 1: if there are no element in the list
        if self.head is None:
            self.head = self.tail = new_node
        # case 2: if there are one or more element in the list
        else:
            new_node.next = self.head
            self.head = new_node
        self.count += 1


linked_list = LinkedList()
linked_list.prepend(4)
linked_list.append(1)
linked_list.print_list()
print(linked_list.count)
