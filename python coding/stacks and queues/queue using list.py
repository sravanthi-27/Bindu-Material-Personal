class Queue:
    def __init__(self):
        self.items = []
        # Time: O(1), Space: O(1)

    def is_empty(self):
        return len(self.items) == 0
        # Time: O(1), Space: O(1)

    def enqueue(self, item):
        self.items.append(item)
        # Time: O(1) amortized, Space: O(1)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
            # Time: O(n), Space: O(1) — because pop(0) shifts all elements
        else:
            return None
            # Time: O(1), Space: O(1)

    def peek(self):
        if not self.is_empty():
            return self.items[0]
            # Time: O(1), Space: O(1)
        else:
            return None
            # Time: O(1), Space: O(1)

    def size(self):
        return len(self.items)
        # Time: O(1), Space: O(1)

    
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print("Queue:", q.items)    # Output: Queue: [1, 2, 3]
print("Dequeued:", q.dequeue()) # Output: Dequeued: 1
print("Queue:", q.items)    # Output: Queue: [2, 3]
print("Front:", q.peek())    # Output: Front: 2
print("Size:", q.size())    # Output: Size: 2