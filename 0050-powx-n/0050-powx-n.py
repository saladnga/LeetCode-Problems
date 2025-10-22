class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 1:
            return x
        if n < 0:
            return 1 / self.myPow(x, -n)
        if n == 0:
            return 1
        half = self.myPow(x, n // 2)
        if n % 2 == 0:
            x = half * half
        else:
            x = half * half * x
        return x