class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_count = defaultdict(int)
        count = 0
        for row in grid:
            row_count[tuple(row)] += 1
        for column in zip(*grid):
            count += row_count[column]
        return count