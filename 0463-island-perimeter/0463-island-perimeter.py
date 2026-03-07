class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        seen = set()
        m, n = len(grid), len(grid[0])

        def dfs(row, col):
            if (row, col) in seen:
                return
            perimeter = 0
            seen.add((row, col))
            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy
                if next_row < 0 or next_row >= m or next_col < 0 or next_col >= n:
                    perimeter += 1
                elif grid[next_row][next_col] == 0:
                    perimeter += 1
                elif (next_row, next_col) not in seen:
                    perimeter += dfs(next_row, next_col)
            return perimeter

        for row in range(m):
            for col in range(n):
                if grid[row][col] == 1 and (row, col) not in seen:
                    return dfs(row, col)