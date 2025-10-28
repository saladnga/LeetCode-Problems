class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        edges = defaultdict(list)
        for u, v, t in flights:
            edges[u].append((v, t))

        minHeap = [(0, src, 0)]
        visited = {}

        while minHeap:
            t1, n1, s1 = heapq.heappop(minHeap)
            if n1 == dst:
                return t1
            if s1 > k:
                continue
            if n1 in visited and visited[n1] <= s1:
                continue
            visited[n1] = s1
            for n2, t2 in edges[n1]:
                heapq.heappush(minHeap, (t1 + t2, n2, s1 + 1))

        return -1            