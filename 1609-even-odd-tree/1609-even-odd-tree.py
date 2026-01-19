# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return False
        deq = deque()
        level = 0
        deq.append(root)
        
        while deq:
            n = len(deq)
            prev_val = None
            for _ in range(n):
                node = deq.popleft()

                if level % 2 == 0:
                    if node.val % 2 == 0:
                        return False
                    if prev_val is not None and node.val <= prev_val:
                        return False
                
                if level % 2 != 0:
                    if node.val % 2 != 0:
                        return False
                    if prev_val is not None and node.val >= prev_val:
                        return False
                
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
                prev_val = node.val

            level += 1
        return True
                    