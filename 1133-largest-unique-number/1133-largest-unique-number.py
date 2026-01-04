class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        count = {}
        res = -1
        for num in nums:
            if num not in count:
                count[num] = 0
            count[num] += 1
        for key in count:
            if count[key] == 1:
                res = max(res, key)
        return res