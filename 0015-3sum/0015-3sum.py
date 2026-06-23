class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        for i, num in enumerate(nums):
            if i > 0 and num == nums[i-1]:
                continue
            left, right = i + 1, len(nums) - 1
            while left < right:
                curr = num + nums[left] + nums[right]
                if curr < 0:
                    left += 1
                elif curr > 0:
                    right -= 1
                else:
                    res.append([num, nums[left], nums[right]])
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -= 1
                    left += 1
                    right -= 1
        return res