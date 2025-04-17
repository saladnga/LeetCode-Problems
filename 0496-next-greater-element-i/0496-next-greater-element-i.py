class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack, ans = [], []
        hash = {}
        for num in nums2:
            while stack and num > stack[-1]:
                hash[stack[-1]] = num
                stack.pop()
            stack.append(num)
        while stack:
            hash[stack[-1]] = -1
            stack.pop()
        for num in nums1:
            ans.append(hash[num])
        return ans
        