class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        ans = []
        curr = 0
        for digit in word:
            curr = (curr * 10 + int(digit)) % m
            if curr == 0:
                ans.append(1)
            else:
                ans.append(0)
        return ans