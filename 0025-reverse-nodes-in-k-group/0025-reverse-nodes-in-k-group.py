# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or k <= 1:
            return head

        curr = head
        prev = None

        while True:
            check = curr
            count = 0
            while check and count < k:
                check = check.next
                count += 1
            if count < k:
                return head


            last_node_prev_part = prev
            last_node_sublist = curr
            i = 0
            while curr and i < k:
                curr_next = curr.next
                curr.next = prev
                prev = curr
                curr = curr_next
                i += 1
            
            if last_node_prev_part:
                last_node_prev_part.next =  prev
            else:
                head = prev
                
            last_node_sublist.next = curr

            if not curr:
                break
            prev = last_node_sublist
        return head
                
            
