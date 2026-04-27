# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def dfs(node, small, large):
            if not node:
                return True
            if not (small < node.val < large):
                return False
            left = dfs(node.left, small, node.val)
            right = dfs(node.right, node.val, large)
            return left and right
        return dfs(root, float("-inf"), float("inf"))