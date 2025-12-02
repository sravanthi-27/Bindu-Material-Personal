class Stack:
    def __init__(self):
        self.items = []
        # Time: O(1), Space: O(1)

    def is_empty(self):
        return len(self.items) == 0
        # Time: O(1), Space: O(1)

    def push(self, item):
        self.items.append(item)
        # Time: O(1), Space: O(1)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
            # Time: O(1), Space: O(1)
        else:
            return None
            # Time: O(1), Space: O(1)

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
            # Time: O(1), Space: O(1)
        else:
            return None
            # Time: O(1), Space: O(1)

    def size(self):
        return len(self.items)
        # Time: O(1), Space: O(1)
s = Stack()

s.push(10)
s.push(20)
s.push(30)

print(s.peek())     # 30
print(s.pop())      # 30
print(s.peek())     # 20
print(s.size())     # 2
print(s.is_empty()) # False
