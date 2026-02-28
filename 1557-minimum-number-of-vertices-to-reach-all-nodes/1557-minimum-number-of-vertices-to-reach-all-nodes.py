class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        result = []
        indegree = [0] * n
        for _, y in edges:
            indegree[y] += 1
        for node in range(n):
            if indegree[node] == 0:
                result.append(node)
        return result