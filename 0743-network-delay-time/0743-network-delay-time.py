class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        visited = set()
        ans = 0
        minHeap = [(0, k)]
        edges = defaultdict(list)

        for u, v, w in times:
            edges[u].append((v, w))
        
        while minHeap:
            w1, n1 = heapq.heappop(minHeap)
            if n1 in visited:
                continue
            visited.add(n1)
            ans = max(ans, w1)
            for n2, w2 in edges[n1]:
                if n2 not in visited:
                    heapq.heappush(minHeap, (w1 + w2, n2))
        
        return ans if len(visited) == n else -1
