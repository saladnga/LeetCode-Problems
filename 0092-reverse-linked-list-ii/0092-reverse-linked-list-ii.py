# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head

        curr = head
        prev = None

        i = 0
        while curr and i < left - 1:
            prev = curr
            curr = curr.next
            i += 1

        last_node_first_part = prev
        last_node_sub_list = curr
        
        i = 0
        while curr and i < right - left + 1:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
            i += 1
        
        if last_node_first_part:
            last_node_first_part.next = prev
        else:
            head = prev

        last_node_sub_list.next = curr
        return head