class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n == 1:
            return nums[0]
        nums.sort()
        currentIndex = n - 1
        while currentIndex >= 0:
            if currentIndex == 0 or nums[currentIndex] != nums[currentIndex - 1]:
                return nums[currentIndex]
            while currentIndex > 0 and nums[currentIndex] == nums[currentIndex - 1]:
                currentIndex -= 1
            currentIndex -= 1
        return -1
