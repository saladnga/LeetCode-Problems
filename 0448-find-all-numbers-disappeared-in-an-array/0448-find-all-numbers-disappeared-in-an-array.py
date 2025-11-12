class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        i = 0
        while i < n:
            correct = nums[i] - 1
            if correct < n and nums[correct] != nums[i]:
                nums[i], nums[correct] = nums[correct], nums[i]
            else:
                i += 1
        for i in range(n):
            if nums[i] != i + 1:
                res.append(i + 1)
        return res