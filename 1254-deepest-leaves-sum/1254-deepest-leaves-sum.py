# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        queue = deque([root])
        res = 0
        while queue:
            res = 0
            for _ in range(len(queue)):
                node = queue.popleft()

                if node.left == None and node.right == None:
                    res += node.val

                if node.left != None:
                    queue.append(node.left)
                if node.right != None:
                    queue.append(node.right)
        return res