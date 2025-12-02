from collections import deque
class Stack:
    def __init__(self):
        self.container = deque()
    def push(self,value):
        self.container.append(value)
    def pop(self):
        return self.container.pop()
    def peek(self):
        return self.container[-1]
    def size(self):
        return len(self.container)
stack = Stack()
s = "We will conquere COVID-19"
for ch in s:
    stack.push(ch)
rev = ''
while stack.size()!=0: #you can also use this for ch in s: but our idea is to implement using stack
    rev+=stack.pop()
print(rev)



















s = "We will conquere COVID-19"
