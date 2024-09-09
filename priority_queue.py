from heap import MaxHeap


class PriorityQueue:

    def __init__(self) -> None:
        self.heap = MaxHeap()

    def enqueue(self, value: int) -> None:
        """
        method to insert an element in on a priority queue.
        """
        self.heap.insert(value)

    def dequeue(self) -> int:
        """
        Method to remove the largest element from a queue.
        """
        return self.heap.remove()

    def is_empty(self) -> bool:
        """
        Helper method to return true if the priority queue is empty.
        """
        return self.heap._is_empty()


priority_queue = PriorityQueue()
priority_queue.enqueue(10)
priority_queue.enqueue(7)
priority_queue.enqueue(22)
priority_queue.dequeue()
priority_queue.dequeue()
priority_queue.dequeue()
priority_queue.dequeue()
print(priority_queue.heap.heap)
