class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        m, n = len(grid), len(grid[0])
        seen = set()
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        # row, col in range and has the same character
        def valid(row, col, char):
            return 0 <= row < m and 0 <= col < n and grid[row][col] == char

        def dfs(row, col, prev_row, prev_col, char):
            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy

                # skip if out of bound
                if not valid(next_row, next_col, char):
                    continue

                # skip if the cell we came from (the parent)
                if next_row == prev_row and next_col == prev_col:
                    continue

                # if already visited and not parent -> cycle found
                if (next_row, next_col) in seen:
                    return True

                # mark as visited and continue dfs
                seen.add((next_row, next_col))
                if dfs(next_row, next_col, row, col, grid[next_row][next_col]):
                    return True
            return False

        # dfs unvisited cells
        for row in range(m):
            for col in range(n):
                if valid(row, col, grid[row][col]) and (row, col) not in seen:
                    seen.add((row, col))
                    # dfs with the current character
                    if dfs(row, col, -1, -1, grid[row][col]):
                        return True

        return False
