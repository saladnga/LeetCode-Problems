# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def modifiedList(self, nums: List[int], head: Optional[ListNode]) -> Optional[ListNode]:
        num_set = set()
        dummy = ListNode(0, head)
        prev = dummy
        curr = head

        for num in nums:
            num_set.add(num)
        
        while curr and curr.next:
            if curr.val in num_set:
                prev.next = curr.next
            else:
                prev = curr
            curr = curr.next

        return dummy.next