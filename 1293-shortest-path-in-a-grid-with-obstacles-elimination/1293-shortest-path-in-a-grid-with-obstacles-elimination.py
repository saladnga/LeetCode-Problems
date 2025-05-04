class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0])
        def valid(row, col):
            return 0 <= row < m and 0 <= col < n
        queue = deque([(0, 0, k, 0)])
        seen = {(0, 0, k)}
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        while queue:
            row, col, remains, steps = queue.popleft()
            if row == m - 1 and col == n - 1:
                return steps
            for dx, dy in directions:
                next_row, next_col = row + dy, col + dx
                if valid(next_row, next_col):
                    if grid[next_row][next_col] == 0:
                        if (next_row, next_col, remains) not in seen:
                            seen.add((next_row, next_col, remains))
                            queue.append((next_row, next_col, remains, steps + 1))
                    elif remains and (next_row, next_col, remains - 1) not in seen:
                        seen.add((next_row, next_col, remains - 1))
                        queue.append((next_row, next_col, remains - 1, steps + 1))
        return -1