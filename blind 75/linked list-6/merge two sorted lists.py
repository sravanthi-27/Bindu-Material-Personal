# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#iteration
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        result = ListNode()  # Dummy node to start the merged list,you're reusing the nodes from list1 and list2.not creatiing extra space
        current = result     # Pointer to build the list,res andc curr have same addrresses so when modifying currr es also modifies

        while list1 and list2:
            if list1.val < list2.val:  # Choose the smaller value
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next  # Move the pointer forward

        # Attach remaining nodes if any list is not fully merged
        if list1:
            current.next = list1 
        if list2:
            current.next = list2

        return result.next  #result is the dummy node. It's not part of the actual data — it's just a starting point.result.next points to the first real node in the merged list.


#recursion
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1, list2):
        if list1 is None:
            return list2
        if list2 is None:
            return list1
        if list1.val <= list2.val:
            list1.next = self.mergeTwoLists(list1.next, list2)
            return list1
        else:
            list2.next = self.mergeTwoLists(list1, list2.next)
            return list2