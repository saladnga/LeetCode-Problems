class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        quad = []
        for i in range(n - 3):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            for j in range(i + 1, n - 2):
                if j > i + 1 and nums[j] == nums[j - 1]:
                    continue
                left, right = j + 1, n - 1
                while left < right:
                    total = nums[i] + nums[j] + nums[left] + nums[right]
                    if total == target:
                        quad.append([nums[i], nums[j], nums[left], nums[right]])
                        left_val = nums[left]
                        right_val = nums[right]
                        while left < right and nums[left] == left_val:
                            left += 1
                        while left < right and nums[right] == right_val:
                            right -= 1
                    elif total < target:
                        left += 1
                    else:
                        right -= 1
        return quad