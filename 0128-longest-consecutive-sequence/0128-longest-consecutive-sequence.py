class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        res = 0
        for num in set_nums:
            if num - 1 not in set_nums:
                start = num
                length = 1
                while start + 1 in set_nums:
                    length += 1
                    start += 1
                res = max(res, length)
        return res