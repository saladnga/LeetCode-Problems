# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 0:
            return head
        
        length = 1
        last_node = head
        while last_node.next:
            last_node = last_node.next
            length += 1
        
        last_node.next = head
        k = k % length
        skip = length - k 

        new_tail = head
        for i in range(skip - 1):
            new_tail = new_tail.next
        new_head = new_tail.next
        new_tail.next = None
        return new_head