class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        x = nums[0]
        ans = 1
        for i in range(1, len(nums)):
            if nums[i] - x > k:
                ans += 1
                x = nums[i]
        return ans