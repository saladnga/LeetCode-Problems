class Solution:
    def smallestNumber(self, n: int) -> int:
        x = n
        while True:
            if x > 0 and (x & (x + 1)) == 0:
                return x
            else:
                x += 1
        return -1