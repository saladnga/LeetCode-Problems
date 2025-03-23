class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        connection = {a : b for a, b in paths}
        start = paths[0][0]
        while start in connection:
            start = connection[start]
        return start