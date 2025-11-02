class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        grid = [[0] * n for _ in range(m)]
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        ans = 0
        for (row, col) in walls:
            grid[row][col] = 1
        for (row, col) in guards:
            grid[row][col] = 2
        for (g_row, g_col) in guards:
            for (dx, dy) in directions:
                row = g_row + dx
                col = g_col + dy
                while 0 <= row < m and 0 <= col < n and grid[row][col] != 1 and grid[row][col] != 2:
                    grid[row][col] = 3
                    row += dx
                    col += dy
        for row in range(m):
            for col in range(n):
                if grid[row][col] == 0:
                    ans += 1
        return ans