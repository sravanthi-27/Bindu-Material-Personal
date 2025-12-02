class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Values for the linked list
values = [1, 2, 3, 4, 5]

# Create nodes
nodes = [Node(val) for val in values]

# Link nodes automatically
for i in range(len(nodes)-1,0,-1): #or (-1,-(len(nodes)),-1)
    nodes[i].next = nodes[i - 1]
    

# Head of the list
head = nodes[-1]

# Print linked list
current = head
while current:
    print(current.val, end="->" if current.next else "")
    current = current.next

#iterative
prev = None
current = head
while current:
    next_node = current.next
    current.next = prev
    prev = current
    current = next_node
print(prev)

#recursion
def reverseList(self, head):
    if not head:
        return None

    newHead = head  # Default, in case it's the last node
    if head.next:
        newHead = self.reverseList(head.next)
        head.next.next = head
    head.next = None

    return newHead 
