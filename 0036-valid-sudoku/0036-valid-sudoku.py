class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        seen = set()
        for r in range(9):
            for c in range(9):
                val = board[r][c]
                if val != ".":
                    row_key = ("row", r, val)
                    col_key = ("col", c, val)
                    sub_box_key = ("box", ((r // 3) * 3 + (c //3)), val)
                    if row_key in seen or col_key in seen or sub_box_key in seen:
                        return False
                    seen.update({row_key, col_key, sub_box_key})
        return True
        