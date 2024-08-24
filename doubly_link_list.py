class _Node:

    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.previous = None


class DoublyLinkList(_Node):

    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.length = 0

    def print_list(self) -> None:
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def append(self, value) -> bool:
        new_node = _Node(value)
        # case 1: if there are no items in the link list
        if self.head is None:
            self.head = self.tail = new_node
        # case 2: if there are one or more elements in the DLL
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def pop(self) -> _Node | None:
        # case 1: if the list is empty
        if self.length == 0:
            return None
        # case 2: if there are one item in the list
        current = self.tail
        if self.length == 1:
            self.head = self.tail = None
        # if there are more than one element in the list
        else:
            self.tail = self.tail.previous
            self.tail.next = None
            current.previous = None
        self.length -= 1
        return current

    def prepend(self, value) -> bool:
        new_node = _Node(value)
        # case 1: when there are no items in the list
        if self.head is None:
            self.head = self.tail = new_node
        # case 2: if there are one ore more items in the list
        else:
            self.head.previous = new_node
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self) -> _Node | None:
        # case 1: there are no elemets in the list.
        if self.head is None:
            return None
        current = self.head
        # case 2: if there are one element in the list.
        if self.length == 1:
            self.head = self.tail = None
        # case 3: if there are more than one elemets in the list
        else:
            self.head = self.head.next
            current.next = None
            self.head.previous = None
        self.length -= 1
        return current

    def get(self, index) -> _Node | None:
        #  case 1: if the index is out of range
        if index < 0 or index >= self.length:
            return None
        current = self.head
        # case 2: the index is valid then find the index
        #  if the index is in the first half of the list start from first
        if index < self.length/2:
            for _ in range(index):
                current = current.next
        #  if index is in the second half of the list then start from last
        else:
            current = self.tail
            for _ in range(self.length - 1, index, -1):
                current = current.previous
        return current

    def set(self, value, index) -> bool:
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False

    def contains(self, value) -> bool:
        current = self.head
        while current:
            if current.value == value:
                return True
            current = current.next
        return False

    def index_of(self, value) -> _Node | None:
        index = 0
        current = self.head
        while current:
            if current.value == value:
                return index
            current = current.next
            index += 1
        return None

    def insert_at(self, index, value) -> bool:
        # case 1: check if index is valid index
        if index < 0 or index > self.length:
            return None
        # case 2: if insert at th beginning
        if index == 0:
            return self.prepend(value=value)
        # case 3: if index is at the end
        if index == self.length:
            return self.append(value=value)
        # case 4: if insert at the middle
        new_node = _Node(value=value)
        after = self.get(index)
        before = after.previous
        new_node.previous = before
        new_node.next = after
        before.next = new_node
        after.previous = new_node
        self.length += 1
        return True

    def remove_at(self, index) -> bool:
        # case 1: cehck if the index is a valid index or not.
        if index < 0 or index >= self.length:
            return None
        # case 2: if remove from first
        if index == 0:
            return self.pop_first()
            # case 3: if remove from last
        if index == self.length - 1:
            return self.pop()
        # case 4: remove value from middle
        node = self.get(index)
        node.previous.next = node.next
        node.next.previous = node.previous
        node.previous = None
        node.next = None
        self.length -= 1
        return node.value


ddl = DoublyLinkList()
ddl.append(2)
ddl.append(3)
ddl.append(10)
ddl.append(20)
ddl.append(30)
ddl.append(40)
ddl.remove_at(4)
ddl.print_list()
