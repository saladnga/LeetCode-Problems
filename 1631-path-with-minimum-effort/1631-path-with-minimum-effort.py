class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        m, n = len(heights), len(heights[0])
        left = 0
        right = max(max(row) for row in heights)
        def valid(row, col):
            return 0 <= col < n and 0 <= row < m
        def check(effort):
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            seen = {(0, 0)}
            stack = [(0, 0)]
            while stack:
                row, col = stack.pop()
                if (row, col) == (m - 1, n - 1):
                    return True
                for dx, dy in directions:
                    next_row, next_col = row + dx, col + dy
                    if valid(next_row, next_col) and (next_row, next_col) not in seen:
                        if abs(heights[next_row][next_col] - heights[row][col]) <= effort:
                            seen.add((next_row, next_col))
                            stack.append((next_row, next_col))
            return False

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left