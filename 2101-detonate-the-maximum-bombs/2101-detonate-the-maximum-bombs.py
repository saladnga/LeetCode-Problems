class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        adj = defaultdict(list)
        for i in range(len(bombs)):
            for j in range(i + 1, len(bombs)):
                x1, y1, r1 = bombs[i]
                x2, y2, r2 = bombs[j]
                d = sqrt((x2 - x1)**2 + (y2 - y1)**2)
                if d <= r1:
                    adj[i].append(j)
                if d <= r2:
                    adj[j].append(i)

        def dfs(i, visit):
            if i in visit:
                return 0
            visit.add(i)
            for neighbor in adj[i]:
                dfs(neighbor, visit)
            return len(visit)

        result = 0
        for i in range(len(bombs)):
            visit = set()
            result = max(result, dfs(i, visit))
        return result