class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        def check(mid):
            count = 1
            current_sum = 0
            for num in nums:
                if current_sum + num > mid:
                    count += 1
                    current_sum = num
                else:
                    current_sum += num
            return count <= k
        
        left = max(nums)
        right = sum(nums)
        ans = right

        while left <= right:
            mid = (left + right) // 2
            if check(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans