# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        def dfs(curr, currPath):
            if not curr:
                return 0
            currPath.append(curr.val)
            pathSum, pathCount = 0, 0
            for i in range(len(currPath) - 1, -1, -1):
                pathSum += currPath[i]
                if pathSum == targetSum:
                    pathCount += 1
            pathCount += dfs(curr.left, currPath)
            pathCount += dfs(curr.right, currPath)
            currPath.pop()
            return pathCount
        return dfs(root, [])