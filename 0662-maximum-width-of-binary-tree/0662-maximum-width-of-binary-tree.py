# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        deq = deque()
        deq.append((root, 0))
        maxWidth = 0
        while deq:
            min_index = deq[0][1]
            first = last = 0
            size = len(deq)
            for i in range(size):
                node, index = deq.popleft()
                index -= min_index
                if i == 0:
                    first = index
                if i == size - 1:
                    last = index
                if node.left:
                    deq.append((node.left, 2 * index))
                if node.right:
                    deq.append((node.right, 2 * index + 1))
            maxWidth = max(maxWidth, last - first + 1)
        return maxWidth