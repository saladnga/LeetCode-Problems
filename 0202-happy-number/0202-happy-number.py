class Solution:
    def isHappy(self, n: int) -> bool:
        def findSquare(n):
            total = 0
            while n > 0:
                digit = n % 10
                total += digit * digit
                n //= 10
            return total
        slow, fast = n, n
        while True:
            slow = findSquare(slow)
            fast = findSquare(findSquare(fast))
            if slow == fast:
                break
        return slow == 1
