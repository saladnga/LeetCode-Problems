class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        while left <= right:
            pivot = (left + right) // 2
            if target == nums[pivot]:
                return pivot
            elif target <= nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
        return left