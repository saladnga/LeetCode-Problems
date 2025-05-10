class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        def neighbors(node):
            ans = []
            for i in range(4):
                num = int(node[i])
                for change in [-1, 1]:
                    x = (num + change) % 10
                    ans.append(node[:i] + str(x) + node[i + 1:])
            return ans
        
        if "0000" in deadends:
            return -1
        
        queue = deque([("0000", 0)])
        seen = set(deadends)
        seen.add("0000")

        while queue:
            node, steps = queue.popleft()
            if node == target:
                return steps
            for neighbor in neighbors(node):
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append((neighbor, steps + 1))

        return -1