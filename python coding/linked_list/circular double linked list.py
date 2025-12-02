class Node: #circular double linked list
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class CircularLinkedList:
    def __init__(self):
        self.head = None   # Initially, the list is empty, so head is None

    def insert_at_beginning(self, data):
        new_node = Node(data)  # Create a new node with the given data
    
        if self.head is None:  # If the list is empty
            new_node.next = new_node  # Point it to itself (because it’s circular)
            self.head = new_node      # This node becomes the head of the list
            return
    
        itr = self.head            # Start from the head
        while itr.next != self.head:  # Traverse to the last node
            itr = itr.next
    
        new_node.next = self.head  # New node points to old head
        itr.next = new_node        # Last node now points to the new node
        self.head = new_node       # New node becomes the new head
    
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            new_node.next = new_node 
            new_node.prev = new_node
            self.head = new_node
            return

        itr = self.head
        while itr.next != self.head:
            itr = itr.next

        itr.next = new_node
        new_node.next = self.head

    def insert_at_index(self, index, data):
        if index <0:
            print("Invalid index")
            return

        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 1
        itr = self.head
        while itr.next != self.head and count < index:
            itr = itr.next
            count += 1

        if count != index:
            print("Index out of range")
            return

        new_node = Node(data)
        new_node.next = itr.next
        itr.next = new_node

    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
            return

        itr = self.head
        while itr.next != self.head:
            itr = itr.next

        itr.next = self.head.next # Last node points to second node
        self.head = self.head.next #head moves to second node

    def delete_at_end(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
            return

        prev = None
        itr = self.head
        while itr.next != self.head:
            prev = itr
            itr = itr.next

        prev.next = self.head #removing last node by pointing prev to head

    def delete_at_index(self, index):
        if self.head is None:
            print("List is empty")
            return

        if index == 0:
            self.delete_at_beginning()
            return

        count = 1
        prev = self.head
        itr = self.head.next

        while itr != self.head and count < index:
            prev = itr
            itr = itr.next
            count += 1

        if itr == self.head: #it means we are completing one full cycle and never found that index
            print("Index out of range")
            return

        prev.next = itr.next #skip over the node to delete

    def count(self):
        if self.head is None:
            return 0

        count = 1
        itr = self.head
        while itr.next != self.head:
            count += 1
            itr = itr.next
        return count

    def print_list(self):
        if self.head is None:
            print("List is empty")
            return

        itr = self.head
        while True:
            print(itr.data, end=" -> ")
            itr = itr.next
            if itr == self.head:
                break
        print("(back to head)")

    def print_backward(self):
        if self.head is None:
            print("List is empty")
            return

        itr = self.head.prev  # Start from last node
        while True:
            print(itr.data, end=" <-> ")
            itr = itr.prev
            if itr == self.head.prev:
                break
        print("(back to tail)")

# Example test
if __name__ == "__main__":
    cll = CircularLinkedList()
    cll.insert_at_end(10)
    cll.insert_at_end(20)
    cll.insert_at_beginning(5)
    cll.insert_at_index(2, 15)
    cll.print_list()
    print("Count:", cll.count())

    cll.delete_at_index(2)
    cll.delete_at_end()
    cll.delete_at_beginning()
    cll.print_list()
    print("Count:", cll.count())
    cll.print_backward()