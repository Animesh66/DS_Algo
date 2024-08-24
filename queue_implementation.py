class _Node:

    def __init__(self, value) -> None:
        self.value = value
        self.next = None


class Queue(_Node):

    def __init__(self) -> None:
        self.first = None
        self.last = None
        self.length = 0

    def print_queue(self) -> None:
        current = self.first
        while current:
            print(current.value)
            current = current.next

    def enque(self, value) -> bool:
        new_node = _Node(value=value)
        # case 1: verify if the queue is empty
        if self.first is None:
            self.first = self.last = new_node
        # case 2: if there are more than one element in the queue
        else:
            self.last.next = new_node
            self.last = new_node
        self.length += 1
        return True

    def deque(self) -> _Node | None:
        # case 1: check if the queue is empty or not
        if self.first is None:
            return None
        current = self.first
        # case 2: if there are only one item in queue
        if self.length == 1:
            self.first = self.last = None
        # case 3: check if the queue is more than one element in queue
        else:
            self.first = self.first.next
            current.next = None
        self.length -= 1
        return current


queue = Queue()
queue.enque(10)
queue.enque(20)
queue.enque(30)
queue.deque()
queue.deque()
queue.deque()
queue.print_queue()

