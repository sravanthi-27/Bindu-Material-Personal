class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None  # Points to front node
        self.rear = None   # Points to rear node
        self._size = 0     # Track size

    def is_empty(self):
        return self.front is None
        # Time: O(1), Space: O(1)

    def enqueue(self, item):
        new_node = Node(item)
        if self.rear is None:
            # Queue empty, front and rear point to new node
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node
        self._size += 1
        # Time: O(1), Space: O(1)

    def dequeue(self):
        if self.is_empty():
            return None
        removed_data = self.front.data
        self.front = self.front.next
        if self.front is None:
            # Queue became empty, update rear too
            self.rear = None
        self._size -= 1
        return removed_data
        # Time: O(1), Space: O(1)

    def peek(self):
        if self.is_empty():
            return None
        return self.front.data
        # Time: O(1), Space: O(1)

    def size(self):
        return self._size
        # Time: O(1), Space: O(1)

    def get_all_elements(self):
        """Return a list of all elements from front to rear"""
        elements = []
        current = self.front
        while current:
            elements.append(current.data)
            current = current.next
        return elements

    def print_queue(self):
        """Print all elements in queue from front to rear"""
        elements = self.get_all_elements()
        print("Queue:", elements)
q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

q.print_queue()             # Output: Queue: [1, 2, 3]
print("Dequeued:", q.dequeue()) # Output: Dequeued: 1
q.print_queue()             # Output: Queue: [2, 3]
print("Front:", q.peek())   # Output: Front: 2
print("Size:", q.size())    # Output: Size: 2
