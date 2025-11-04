class Solution:
    def findXSum(self, nums: List[int], k: int, x: int) -> List[int]:
        n = len(nums)
        size = n - k + 1
        ans = []
        for i in range(size):
            window = nums[i: i + k]
            freq = Counter(window)
            freq_sorted = sorted(freq.items(), key=lambda item: (-item[1], -item[0]))
            top_x = set(num for num, _ in freq_sorted[:x])
            sum_x = sum(num for num in window if num in top_x)
            ans.append(sum_x)
        return ans