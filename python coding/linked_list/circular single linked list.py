class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)

        if self.head is None:
            new_node.next = new_node  # Points to itself
            self.head = new_node
            return

        # Find last node
        itr = self.head
        while itr.next != self.head:
            itr = itr.next

        new_node.next = self.head
        itr.next = new_node
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            new_node.next = new_node
            self.head = new_node
            return

        itr = self.head
        while itr.next != self.head:
            itr = itr.next

        itr.next = new_node
        new_node.next = self.head

    def insert_at_index(self, index, data):
        if index < 0:
            print("Invalid index")
            return

        if index == 0:
            self.insert_at_beginning(data)
            return

        new_node = Node(data)
        count = 1
        itr = self.head

        while itr.next != self.head and count < index:
            itr = itr.next
            count += 1

        if count != index:
            print("Index out of range")
            return

        new_node.next = itr.next
        itr.next = new_node

    def delete_at_beginning(self):
        if self.head is None:
            print("List is empty")
            return

        if self.head.next == self.head:
            self.head = None
            return

        last = self.head
        while last.next != self.head:
            last = last.next

        last.next = self.head.next
        self.head = self.head.next

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

        prev.next = self.head

    def delete_at_index(self, index):
        if self.head is None:
            print("List is empty")
            return

        if index == 0:
            self.delete_at_beginning()
            return

        count = 1
        prev = self.head
        curr = self.head.next

        while curr != self.head and count < index:
            prev = curr
            curr = curr.next
            count += 1

        if curr == self.head:
            print("Index out of range")
            return

        prev.next = curr.next

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

        #we cant do bcakward traversal but it is possible using a list and reversing it
    def print_backward(self):
        if self.head is None:
            print("List is empty")
            return
    
        result = []
        itr = self.head
    
        while True:
            result.append(itr.data)
            itr = itr.next
            if itr == self.head:
                break
    
        for data in reversed(result):
            print(data, end=" <- ")
        print("(back to tail)")


# ---------------- Example Test ---------------- #
if __name__ == "__main__":
    cll = CircularSinglyLinkedList()
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
