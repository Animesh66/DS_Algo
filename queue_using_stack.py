from stack import Stack

# queue = [10, 20, 30]
# stack_enqueue = [ 10, 20, 30]
# stack_dequeue = []


class QueueUsingStack:

    stack_enqueue = Stack()
    stack_dequeue = Stack()

    def enqueue(self, value):
        self.stack_enqueue.push(value)

    def dequeue(self):
        if self.is_empty():
            return None
        if self.stack_dequeue.is_empty():
            while not self.stack_enqueue.is_empty():
                self.stack_dequeue.push(self.stack_enqueue.pop())
        return self.stack_dequeue.pop()

    def is_empty(self):
        return self.stack_dequeue.is_empty() and self.stack_enqueue.is_empty()

    def peek(self):
        if self.is_empty():
            return None
        if self.stack_dequeue.is_empty():
            while not self.stack_enqueue.is_empty():
                self.stack_dequeue.push(self.stack_enqueue.pop())
        return self.stack_dequeue.peek()

    def print_queue(self):
        current = self.stack_enqueue.top
        while current:
            print(current.value)
            current = current.next


queue = QueueUsingStack()
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
