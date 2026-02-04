# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        def findAll(curr, targetSum, currPath, allPaths):
            if not curr:
                return None
            currPath.append(curr.val)
            if curr.val == targetSum and not curr.left and not curr.right:
                allPaths.append(list(currPath))
            else:
                findAll(curr.left, targetSum - curr.val, currPath, allPaths)
                findAll(curr.right, targetSum - curr.val, currPath, allPaths)
            currPath.pop()
        allPaths = []
        findAll(root, targetSum, [], allPaths)
        return allPaths