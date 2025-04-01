# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        if head == None or head.next == None:
            return None
        fast = head
        slow = head
        while fast != None:
            fast = fast.next.next
            slow = slow.next
        prev = None
        curr = slow
        nextNode = None
        while curr != None:
            nextNode = curr.next
            curr.next = prev
            prev = curr
            curr = nextNode
        secondHalf = prev
        maxSum = 0
        while secondHalf != None:
            maxSum = max(maxSum, head.val + secondHalf.val)
            head = head.next
            secondHalf = secondHalf.next
        return maxSum
