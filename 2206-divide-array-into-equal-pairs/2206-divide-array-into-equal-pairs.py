class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        odd_set = set()
        for num in nums:
            if num not in odd_set:
                odd_set.add(num)
            else:
                odd_set.remove(num)
        return len(odd_set) == 0