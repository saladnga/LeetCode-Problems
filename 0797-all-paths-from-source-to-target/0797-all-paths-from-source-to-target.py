class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        # [[1,2],[3],[3],[]]
        # target = 3

        ans = []
        target = len(graph) - 1
        def backtrack(currNode, path):
            if currNode == target:
                ans.append(path.copy())
                return
            for nextNode in graph[currNode]:
                path.append(nextNode)
                backtrack(nextNode, path)
                path.pop()
        backtrack(0, [0])
        return ans