# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(head):
            prev = None
            curr = head
            while curr:
                next_node = curr.next
                curr.next = prev
                prev = curr
                curr = next_node
            return prev

        num1, num2 = 0, 0
        l1r = reverse(l1)
        l2r = reverse(l2)
        curr1, curr2 = l1r, l2r
        
        while curr1:
            num1 = num1 * 10 + curr1.val
            curr1 = curr1.next
        while curr2:
            num2 = num2 * 10 + curr2.val
            curr2 = curr2.next

        num3 = num1 + num2
        str_num3 = str(num3)
        
        dummy_head = ListNode()
        curr = dummy_head
        for digit in str_num3[::-1]:
            curr.next = ListNode(int(digit))
            curr = curr.next
        return dummy_head.next
