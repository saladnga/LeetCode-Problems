class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        res = 0
        MOD = 10**9 + 7
        stack = []
        n = len(arr)

        for i in range(n + 1):
            curr = arr[i] if i < n else 0

            while stack and arr[stack[-1]] > curr:
                mid = stack.pop()
                left = stack[-1] if stack else -1
                right = i
                count = (mid - left) * (right - mid)
                res = (res + count * arr[mid]) % MOD
            
            stack.append(i)
        return res