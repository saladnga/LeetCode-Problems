class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:
        length = len(board)
        board.reverse()
        def IntToPos(square):
            row = (square - 1) // length
            col = (square - 1) % length
            if row % 2 != 0:
                col = length - 1 - col
            return [row, col]
        queue = deque()
        queue.append([1, 0])
        visit = set()
        while queue:
            square, moves = queue.popleft()
            for i in range(1, 7):
                nextSquare = square + i
                row, col = IntToPos(nextSquare)
                if board[row][col] != -1:
                    nextSquare = board[row][col]
                if nextSquare == length * length:
                    return moves + 1
                if nextSquare not in visit:
                    visit.add(nextSquare)
                    queue.append([nextSquare, moves + 1])
        return -1