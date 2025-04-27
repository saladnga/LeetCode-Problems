class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        seen = set()
        ans = []
        m = len(grid)
        n = len(grid[0])

        def valid(row, col):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == 1

        def dfs(row, col):
            count = 1
            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    seen.add((next_row, next_col))
                    count += dfs(next_row, next_col)
            return count
        
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and (row, col) not in seen:
                    seen.add((row, col))
                    size = dfs(row, col)
                    ans.append(size)
        
        return max(ans) if ans else 0