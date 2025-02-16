# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        def dfs(root):
            if root == None:
                return 0
            if root.left == None:
                return 1 + dfs(root.right)
            if root.right == None:
                return 1 + dfs(root.left)
            if root.left != None and root.right != None:
                return 1 + min(dfs(root.left), dfs(root.right))
        return dfs(root)