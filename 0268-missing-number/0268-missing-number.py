class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums_set = set(nums)
        n = len(nums) + 1
        for number in range(n):
            if number not in nums_set:
                return number