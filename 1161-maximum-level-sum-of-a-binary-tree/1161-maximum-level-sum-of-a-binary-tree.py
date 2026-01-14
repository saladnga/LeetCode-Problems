# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        deq = deque()
        deq.append(root)
        max_sum = float("-inf")
        max_level = 1
        level = 1

        while deq:
            size = len(deq)
            curr_sum = 0
            for _ in range(size):
                node = deq.popleft()
                curr_sum += node.val
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
            if max_sum < curr_sum:
                max_sum = curr_sum
                max_level = level
            level += 1
        return max_level