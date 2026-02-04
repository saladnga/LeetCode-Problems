# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0 
        def helper(curr, currSum, allPaths):
            if not curr:
                return 0
            currSum = currSum * 10 + curr.val
            if not curr.left and not curr.right:
                allPaths.append(currSum)
            else:
                helper(curr.left, currSum, allPaths)
                helper(curr.right, currSum, allPaths)
        allPaths = []
        helper(root, 0, allPaths)
        return sum(allPaths)