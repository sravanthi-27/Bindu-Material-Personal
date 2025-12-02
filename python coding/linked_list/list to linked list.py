class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def list_to_linkedlist(arr):
    if not arr:  # If list is empty, return None
        return None
    
    head = ListNode(arr[0])  # First node
    current = head
    
    for value in arr[1:]:
        current.next = ListNode(value)  # Create next node
        current = current.next           # Move current
    
    return head  # Return head of the linked list