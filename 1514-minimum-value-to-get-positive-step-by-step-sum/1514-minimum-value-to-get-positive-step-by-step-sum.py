class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        total = 0
        minVal = 0
        for num in nums:
            total += num
            minVal = min(minVal, total)
        return (-minVal) + 1