class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        set_nums2 = set(nums2)
        smallest = math.inf
        for num in nums1:
            if num in set_nums2 and num < smallest:
                smallest = num
        if smallest != math.inf:
            return smallest
        else:
            return -1