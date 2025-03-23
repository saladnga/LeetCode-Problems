class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        num_set = set()
        duplicates = set()
        for num in nums:
            if num not in num_set and num not in duplicates:
                num_set.add(num)
            elif num in num_set:
                num_set.remove(num)
                duplicates.add(num)
        num_list = list(num_set)
        sum = 0
        for i in range(len(num_list)):
            sum += num_list[i]
        return sum