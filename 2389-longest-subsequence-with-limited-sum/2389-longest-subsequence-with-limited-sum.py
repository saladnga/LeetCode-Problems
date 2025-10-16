class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        prefix = [0] * len(nums)
        prefix[0] = nums[0]
        for i in range(1, len(nums)):
            prefix[i] = prefix[i - 1] + nums[i] #prefix formula

        def binary_search(arr, target):
            left, right = 0, len(arr) - 1
            while left <= right:
                mid = (left + right) // 2
                num = arr[mid]
                if num > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return left

        ans = []
        for query in queries:
            i = binary_search(prefix, query)
            ans.append(i)
        return ans
        