class Node:
    def __init__(self,val):
        self.val = val
        self.next = None 
node1 = Node(1)
node2 = Node(2)
node3 = Node(3)
node1.next = node2
node2.next = node3 
current = node1 
while current:
    print(current.val,end="")
    if current.next:
        print("->",end="")
    current = current.next

#2nd way
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

# Values for the linked list
values = [1, 2, 3, 4]

# Create nodes
nodes = [Node(val) for val in values]

# Link nodes automatically
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]

# Head of the list
head = nodes[0]

# Print linked list
current = head
while current:
    print(current.val, end="->" if current.next else "")
    current = current.next
