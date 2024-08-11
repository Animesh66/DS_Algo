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
            self.count = 1
        # if there are already items in the link list
        self.tail.next = new_node
        self.tail = new_node
        self.count += 1

    def pop(self):
        """
        Method for removing element at the end of link list
        """
        # case 1: if there are no items in the link list

        # case 2: if there are only one item in the link list

        # case 3: if there are more than one item in the link list


linked_list = LinkedList()
linked_list.append(3)
linked_list.append(4)
linked_list.append(5)
linked_list.print_list()
