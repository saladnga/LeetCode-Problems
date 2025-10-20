class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        direction = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def valid(row, col):
            return 0 <= row < m and 0 <= col < n

        def backtrack(row, col, i, seen):
            if i == len(word):
                return True

            for dx, dy in direction:
                next_row = row + dy
                next_col = col + dx
                if valid(next_row, next_col) and (next_row, next_col) not in seen:
                    if board[next_row][next_col] == word[i]:
                        seen.add((next_row, next_col))
                        if backtrack(next_row, next_col, i + 1, seen):
                            return True
                        seen.remove((next_row, next_col))
            return False
        
        for row in range(m):
            for col in range(n):
                if board[row][col] == word[0] and backtrack(row, col, 1, {(row, col)}):
                    return True
        return False