class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        result = []
        for i in range(0, m):
            result.append(nums1[i])
        for j in range(0, n):
            result.append(nums2[j])
        result = sorted(result)
        for i in range(len(result)):
            nums1[i] = result[i]
                
        