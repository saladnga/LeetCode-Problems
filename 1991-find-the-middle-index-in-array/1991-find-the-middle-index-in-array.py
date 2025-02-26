class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        n = len(nums)
        left = 0
        sum = 0
        
        if (n == 0):
            return -1

        for i in range(0, len(nums)):
            sum += nums[i]
        
        for i in range(0, len(nums)):
            sum -= nums[i]
            if sum == left:
                return i
            left += nums[i]
            
        return -1