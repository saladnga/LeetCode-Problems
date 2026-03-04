class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        original_color = image[sr][sc]
        
        if image[sr][sc] == color:
            return image
        
        def valid(row, col):
            return 0 <= row < len(image) and 0 <= col < len(image[0]) and image[row][col] == original_color
        
        def dfs(row, col):
            for dx, dy in directions:
                next_row, next_col = row + dx, col + dy
                image[row][col] = color
                if valid(next_row, next_col):
                    dfs(next_row, next_col)
        
        dfs(sr, sc)
        return image
        