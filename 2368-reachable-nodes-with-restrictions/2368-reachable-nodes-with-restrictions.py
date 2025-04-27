class Solution:
    def reachableNodes(self, n: int, edges: List[List[int]], restricted: List[int]) -> int:
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        seen = set()
        restricted_set = set(restricted)
        def dfs(node):
            seen.add(node)
            for neighbor in graph[node]:
                if neighbor not in seen and neighbor not in restricted_set:
                    seen.add(neighbor)
                    dfs(neighbor)
        dfs(0)
        return len(seen)
