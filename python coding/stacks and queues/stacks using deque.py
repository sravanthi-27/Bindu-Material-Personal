from collections import deque
#stack = deque()
#dir(stack) #used to know all methods availab;e
#stack.append("bindu")
#stack.pop()
#print(stack)
class Stack:
    def __init__(self):
        self.container = deque()
    def push(self,val):
        self.container.append(val) #O(1)
    def pop(self):
        if not self.is_empty():
            return self.container.pop()
        else:
            return None             #O(1)
    def peek(self):
        if not self.is_empty():
            return self.container[-1]
        else:
            return None
    def is_empty(self):
        return len(self.container)==0  #O(1)
    def size(self):
        return len(self.container)  #O(1)
    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack:", stack.container)  #if you just use print(stack) it returns address so use stack.container
print("Top element:", stack.peek())
print("Popped element:", stack.pop())
print("Stack after pop:", stack.container)
print("Is stack empty?", stack.is_empty())
print("Stack size:", stack.size())