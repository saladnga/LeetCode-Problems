class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = {}
        for num in nums:
            if num not in seen:
                seen[num] = 0
            seen[num] += 1
        ans = []
        for key, value in seen.items():
            if value == 2:
                ans.append(key)
        return ans