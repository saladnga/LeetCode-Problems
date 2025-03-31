class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        totalCount = 0
        currentSum = 0
        freq = {0: 1}

        for num in nums:
            currentSum += num
            # if currentSum == goal:
            #     totalCount += 1
            prefix = currentSum - goal
            if prefix in freq:
                totalCount += freq[prefix]
            freq[currentSum] = freq.get(currentSum, 0) + 1
        return totalCount
            