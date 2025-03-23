class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x = 0
        y = 0
        current = set([(x, y)])
        points = {'N': (0, 1), 'S': (0, -1), 'E': (-1, 0), 'W': (1, 0)}
        for direction in path:
            dx, dy = points[direction]
            x += dx
            y += dy
            if (x, y) in current:
                return True
            current.add((x, y))
        return False