class _Node:
    def __init__(self, item) -> None:
        self.item = item
        self.next = None


class LinkedList(_Node):
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self) -> None:
        current = self.head
        while (current):
            print(current.item)
            current = current.next

    def append(self, item) -> None:
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
        self.length += 1
        return True

    def pop(self) -> _Node | None:
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
        self.length -= 1
        # case 3: if there are only one item in the link list
        if self.length == 0:
            self.head = self.tail = None
        return current

    def prepend(self, item) -> bool:
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
        self.length += 1
        return True

    def pop_first(self) -> _Node | None:
        """
        Method for removing the first element from the list
        """
        # case 1: if the list is empty
        if self.head is None:
            return None
        # case 2: if list have muliple elements
        else:
            current = self.head
            self.head = self.head.next
            current.next = None
            self.length -= 1
            return current
        # case 3: if the list have only have one element
        if self.length == 0:
            self.head = self.tail = None

    def get_by_index(self, index) -> _Node | None:
        """
        returns the element at the given index 
        Args:
            index (index): index to be given 
        """
        # case 1: check if the given index is valid or not
        if index < 0 or index >= self.length:
            return None
        # case 2: if the index is a valid index
        current = self.head
        for _ in range(index):
            current = current.next
        return current

    def set_value_by_index(self, value, index) -> bool:
        """
        Set the value at the given index
        Args:
            value (int): value to be set
            index (int): the index at which the value is to be set
        """
        current = self.get_by_index(index)
        if current:
            current.item = value
            return True
        return False

    def insert(self, value, index) -> bool:
        """
        insert a particular value at a particular index
        Args:
            value (int): the value to be inserted 
            index (int): at the index this to be inserted
        """
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = _Node(value)
        previous = self.get_by_index(index - 1)
        new_node.next = previous.next
        previous.next = new_node
        self.length += 1
        return True

    def remove(self, index) -> _Node | None:
        """
        remove an item from a particular index.
        Args:
            index (int):the item that should be removed form the given index
        """
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == (self.length - 1):
            return self.pop()
        previous = self.get_by_index(index - 1)
        current = previous.next
        previous.next = current.next
        current.next = None
        self.length -= 1
        return current

    def index_of(self, value) -> int | None:
        """
        return the index of the first occurance of the particular item
        Args:
            value (int): the item for search
        """
        current = self.head
        index = 0
        while current:
            if current.item == value:
                return index
            index += 1
            current = current.next
        return None

    def contains(self, value) -> bool:
        """
        Method returns if the given value is present in the list
        Args:
            value (int): the value to found
        """
        return True if self.index_of(value) is not None else False


linked_list = LinkedList()
linked_list.append(10)
linked_list.append(2)
linked_list.append(3)
print(linked_list.contains(1))
