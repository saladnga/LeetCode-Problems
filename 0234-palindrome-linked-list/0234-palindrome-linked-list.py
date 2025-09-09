# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def reverse(head):
            prev = None
            while head:
                tmp = head.next
                head.next = prev
                prev = head
                head = tmp
            return prev

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        second_half = reverse(slow)

        while head and second_half:
            if head.val != second_half.val:
                return False
            head = head.next
            second_half = second_half.next
        
        return True