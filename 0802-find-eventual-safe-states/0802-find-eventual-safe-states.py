class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        result = []
        # 0 for not visited, 1 for visited, 2 for no outgoing edges
        state = [0] * len(graph)
        def dfs(node):
            if state[node] == 2:
                return True
            if state[node] == 1:
                return False
            state[node] = 1
            for neighbor in graph[node]:
                if not dfs(neighbor):
                    return False
            state[node] = 2
            return True
        for i in range(len(graph)):
            if dfs(i):
                result.append(i)
        return sorted(result)