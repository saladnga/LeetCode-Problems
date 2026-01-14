# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        deq = deque()
        res = []
        if not root:
            return []
        deq.append(root)
        while deq:
            level = len(deq)
            curr = []
            for _ in range(level):
                node = deq.popleft()
                curr.append(node.val)
                if node.left:
                    deq.append(node.left)
                if node.right:
                    deq.append(node.right)
            res.append(curr)
        return res[::-1]