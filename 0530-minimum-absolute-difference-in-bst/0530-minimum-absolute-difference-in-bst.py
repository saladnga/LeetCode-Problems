# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        value = []
        ans = float("inf")
        def dfs(node):
            if not node:
                return
            
            left = dfs(node.left)
            value.append(node.val)
            right = dfs(node.right)
        
        dfs(root)
        for i in range(0, len(value)-1):
            ans = min(ans, abs(value[i] - value[i+1]))
        return ans