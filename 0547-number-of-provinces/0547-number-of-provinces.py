class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False] * len(isConnected)
        provinces = 0

        def dfs(city):
            for i in range(len(isConnected)):
                if isConnected[city][i] == 1 and not visited[i]:
                    visited[i] = True
                    dfs(i)
        
        for i in range(len(isConnected)):
            if not visited[i]:
                dfs(i)
                provinces += 1
        
        return provinces