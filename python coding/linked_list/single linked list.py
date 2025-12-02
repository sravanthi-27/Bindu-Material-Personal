#class Node: — This defines a class called Node. Each node is like a box that holds:
#data (some value like a number or string)
#next (a pointer to the next node in the list)
#def __init__(self, data=None, next=None): — This is the constructor method. It runs automatically when you create a new node.
#self.data = data — Stores the actual value in the node.
#self.next = next — Points to the next node in the list. If it's the last node, next will be None.
class Node:
    def __init__(self,data=None,next=None):
        self.data = data 
        self.next = next 
class LinkedList:
    def __init__(self):
        self.head = None  #self.head = None — When you first create a list, it's empty. So the head (starting point) is None.
    def insert_at_beginning(self,data):
        node  = Node(data,self.head) #node = Node(data, self.head) — Create a new node with: data as a value,self.head as the next node
        self.head = node #now the node becomes the head of the list
    def print(self):
        if self.head is None:
            print("linked list is empty")
            return 
        itr = self.head #start from head of the list
        lstr=''
        while itr:  #if you dont want --> to last node then while itr:   
            lstr+=str(itr.data)+'-->'                           #lstr+=str(ittr.data)
            itr = itr.next                                      #if itr.next: #only add --> if there is a next node
        print(lstr)                                                 #lstr+='-->  
                                                                #itr=itr.next                                                           
    def insert_at_end(self,data):
        if self.head is None:
            self.head = Node(data,None)
            return 
        itr = self.head 
        while itr.next:
            itr = itr.next 
        itr.next = Node(data,None)

    #insert at particular index
    def insert_at(self,index,data):
        if index<0 or index>self.get_length():
            raise Exception("Invalid index")
        if index==0:
            self.insert_at_beginning(data)
            return 
        count = 0
        itr = self.head
        while itr:
            if count==index-1:
                node = Node(data,itr.next)
                itr.next = Node 
                break
            itr = itr.next
            count+=1

    #take a list of values as an input and it will create a new linked list 
    def insert_values(self,data_list):
        self.head = None 
        for data in data_list:
            self.insert_at_end(data)

    #insert new data after the first node that has target data
    def insert_after_value(self, target_data, new_data):
        if self.head is None:
            return
    
        itr = self.head
        while itr:
            if itr.data == target_data:
                node = Node(new_data, itr.next)
                itr.next = node
                return
            itr = itr.next

    #Insert new_data before the first node that has target_data.
    def insert_before_value(self, target_data, new_data):
        if self.head is None:
            return
    
        if self.head.data == target_data:
            self.insert_at_beginning(new_data)
            return
    
        itr = self.head
        while itr.next:
            if itr.next.data == target_data:
                node = Node(new_data, itr.next)
                itr.next = node
                return
            itr = itr.next

    #insert unique data
    def insert_unique(self, data):
        if self.head is None: #if list is empty
            self.head = Node(data)  #just add node
            return
    
        itr = self.head
        while itr:
            if itr.data == data: #check if value already exists
                return  # Don't insert duplicates
            if itr.next is None:  #stop at last node
                break
            itr = itr.next
    
        itr.next = Node(data) #if not found, add to end 

    #insert sorted data
    def insert_sorted(self, data):#If the list is empty, or if data is smaller than the first node (like 5 in a 10-20-30 list), insert at the beginning.
        if self.head is None or self.head.data >= data:
            self.insert_at_beginning(data)
            return
    
        itr = self.head #Move through the list until you find a node whose next is greater than or equal to data.
        while itr.next and itr.next.data < data:
            itr = itr.next
    
        node = Node(data, itr.next)
        itr.next = node



    #length of linked list
    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next 
        return count
    #remove element at particular index 

    # Delete node at the start
    def delete_at_start(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return
        self.head = self.head.next  # Move head to next node

    # Delete node at the end
    def delete_at_end(self):
        if self.head is None:
            print("List is empty, nothing to delete.")
            return
        
        if self.head.next is None:
            # Only one node in the list
            self.head = None
            return
        
        current = self.head
        # Traverse until the second last node
        while current.next.next:
            current = current.next
        
        current.next = None  # Remove last node

    def remove_at(self,index):
        if index<0 or index>self.get_length():
            raise Exception("Invalid index")
        if index==0:
            self.head = self.head.next 
            return 
        count = 0
        itr = self.head 
        while itr:
            if count == index-1:
                itr.next = itr.next.next # becuase we are deleting the element so assign the next address of the deleted element
                break
            itr = itr.next
            count+=1
        
if __name__=='__main__':                                         
    l1 = LinkedList()
    l1.insert_values(["b","c","a"])
    l1.insert_at_beginning(5)
    l1.insert_at_beginning(39)
    l1.insert_at_end(75)
    l1.remove_at(2)
    l1.insert_at(0,"apple")
    l1.insert_at(0,"apple")
    l1.insert_after_value("a", 25)
    l1.insert_before_value("a", 15)  # List becomes: 10-->15-->20-->25-->30

    l1.print()
    print(l1.get_length())