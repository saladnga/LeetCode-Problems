class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set_nums = set()
        for num in nums:
            if num not in set_nums:
                set_nums.add(num)
            else:
                return True
        return False