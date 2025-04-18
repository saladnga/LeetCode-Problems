class Solution:
    def countPairs(self, nums: List[int], k: int) -> int:
        count = 0
        i = 0
        for i in range(len(nums)):
            for j in range(1, len(nums)):
                if nums[i] == nums[j] and k % (nums[i] * nums[j]) == 0:
                    count += 1
        return count