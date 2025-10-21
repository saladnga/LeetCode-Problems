class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        ans = []
        if n == 1:
            ans.append(0)
            return

        def backtrack(curr, remaining):
            if remaining == 0:
                ans.append(curr)
                return
            tail = curr % 10
            next_digits = {tail + k, tail - k}
            for next_digit in next_digits:
                if 0 <= next_digit <= 9:
                    backtrack(curr * 10 + next_digit, remaining - 1)

        for digits in range(1, 10):
            backtrack(digits, n - 1)
        return ans