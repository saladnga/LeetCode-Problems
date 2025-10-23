class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        curr = 0
        left, right = 1, 2**(n - 1)
        
        for _ in range(n):
            mid = (left + right) // 2
            if k <= mid:
                right = mid
            else:
                left = mid + 1
                if curr == 1:
                    curr = 0
                else:
                    curr = 1

        return curr