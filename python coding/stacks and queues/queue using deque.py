from collections import deque

class Queue:
    def __init__(self):
        self.container = deque()              # O(1) space

    def enqueue(self, val):
        self.container.append(val)            # O(1) time

    def dequeue(self):
        if not self.is_empty():
            return self.container.popleft()   # O(1) time  #instead od popleft you can also use insert(0,val) and pop
        else:
            return None                       # O(1)

    def peek(self):
        if not self.is_empty():
            return self.container[0]          # O(1)
        else:
            return None                       # O(1)

    def is_empty(self):
        return len(self.container) == 0       # O(1)

    def size(self):
        return len(self.container)            # O(1)

# Usage example
queue = Queue()
queue.enqueue(1)
queue.enqueue({"b":1})
queue.enqueue(3)

print("Queue:", queue.container)             # Output: Queue: deque([1, 2, 3])
print("Front element:", queue.peek())        # Output: Front element: 1
print("Dequeued element:", queue.dequeue())  # Output: Dequeued element: 1
print("Queue after dequeue:", queue.container)  # Output: deque([2, 3])
print("Is queue empty?", queue.is_empty())   # Output: False
print("Queue size:", queue.size())           # Output: 2
