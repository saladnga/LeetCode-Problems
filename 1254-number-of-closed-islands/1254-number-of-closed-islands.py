class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        ans = 0
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        seen = set()
        m, n = len(grid), len(grid[0])

        def dfs(row, col):
            if 0 > row or row >= m:
                return False
            if 0 > col or col >= n:
                return False
            if grid[row][col] == 1:
                return True
            if (row, col) in seen:
                return True
                
            seen.add((row, col))
            isClosed = True
            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy
                if not dfs(next_row, next_col):
                    isClosed = False
            return isClosed

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0 and (row, col) not in seen:
                    if dfs(row, col):
                        ans += 1

        return ans