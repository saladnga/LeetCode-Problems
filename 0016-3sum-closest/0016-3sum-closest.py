class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest_diff = float('inf')
        n = len(nums)
        for i in range(n - 2):
            left = i + 1
            right = n - 1
            while left < right:
                curr_diff = target - nums[i] - nums[left] - nums[right]
                if curr_diff == 0:
                    return target
                if (abs(curr_diff) < abs(closest_diff)) or (abs(curr_diff) == abs(closest_diff) and curr_diff > closest_diff):
                    closest_diff = curr_diff
                if curr_diff > 0:
                    left += 1
                else:
                    right -= 1
        return target - closest_diff