# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        if not root:
            return 0
        def dfs(curr):
            if not curr:
                return 0
            leftMax = dfs(curr.left)
            rightMax = dfs(curr.right)
            leftMax = max(leftMax, 0)
            rightMax = max(rightMax, 0)
            self.res = max(self.res, curr.val + leftMax + rightMax)
            return curr.val + max(leftMax, rightMax)
        dfs(root)
        return self.res