# traverse through forward and backward direction
class Node:
    def __init__(self, data):
        self.data = data
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data) # gives the data and pointers kept to none
        new_node.next = self.head #point to old front

        if self.head:
            self.head.prev = new_node #old front points back

        self.head = new_node  #move head to new box

    def insert_at_end(self, data):
        new_node = Node(data)  # box labeled data,prev and next are none

        if self.head is None:
            self.head = new_node
            return

        itr = self.head
        while itr.next:
            itr = itr.next  #until last node is reached

        itr.next = new_node #assigning new node address to last node
        new_node.prev = itr #assigning last node address to new node 
    
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count
    
    def insert_at_index(self, index, data):
        length = self.get_length()
        if index < 0 or index > length:
            print("Index out of bounds")
            return

        new_node = Node(data)

        if index == 0:
            new_node.next = self.head #point new node's next to old head
            if self.head:
                self.head.prev = new_node #old head's prev back to new node
            self.head = new_node #make the new node the head
            return

        itr = self.head
        count = 0
        while count < index - 1:
            itr = itr.next
            count += 1

        new_node.next = itr.next 
        if itr.next:
            itr.next.prev = new_node
        itr.next = new_node #link current node to new node
        new_node.prev = itr #link new node back to current node

    def print_forward(self):
        itr = self.head
        while itr:
            print(itr.data, end=' <-> ')
            last = itr  # Keep track for reverse print
            itr = itr.next
        print("None")

    def print_backward(self):
        itr = self.head
        if not itr:
            return

        # Go to last node
        while itr.next:
            itr = itr.next
        #noe print from last to first
        while itr:
            print(itr.data, end=' <-> ')
            itr = itr.prev
        print("None")
    
    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty")
            return
    
        if self.head.next is None:
            self.head = None
            return
    
        self.head = self.head.next #move head to next node
        self.head.prev = None #set none to 2nd element bcz deleting 1st element
    
    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
            return   
        if self.head.next is None:
            self.head = None
            return   
        itr = self.head
        while itr.next:
            itr = itr.next
        itr.prev.next = None #setting previous element next pointer to none

    def delete_at_index(self, index):
        if index < 0 or index > self.get_length():
            print("Invalid index")
            return
    
        if self.head is None:
            print("List is empty")
            return
    
        if index == 0:
            self.delete_at_beginning()
            return
    
        itr = self.head
        count = 0
    
        while itr and count < index:
            itr = itr.next
            count += 1
    
        if itr is None:
            print("Index out of bounds")
            return
    
        if itr.next:
            itr.next.prev = itr.prev
        if itr.prev:
            itr.prev.next = itr.next
    

dll = DoublyLinkedList()
dll.insert_at_end(10)
dll.insert_at_end(20)
dll.insert_at_beginning(5)
dll.insert_at_index(1, 10)
dll.print_forward()     # 5 <-> 10 <-> 20 <-> None
dll.print_backward()    # 20 <-> 10 <-> 5 <-> None

