class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        return self.dfs(arr, start, visited)
    def dfs(self, arr: List[int], start: int, visited: set) -> bool:
        if (start < 0 or start >= len(arr) or start in visited):
            return False
        if (arr[start] == 0):
            return True
        visited.add(start)
        return self.dfs(arr, start + arr[start], visited) or self.dfs(arr, start - arr[start], visited)
        