"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        deq = deque()
        deq.append(root)
        values = []
        while deq:
            n = len(deq)
            curr = []
            for _ in range(n):
                node = deq.popleft()
                curr.append(node.val)
                if node.children:
                    for child in node.children:
                        deq.append(child)
            values.append(curr)
        return values