class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        def get_digit_sum(num):
            digit_sum = 0
            while num > 0:
                digit_sum += num % 10
                num //= 10
            return digit_sum
        ans = -1
        dict_nums = defaultdict(int)
        for num in nums:
            digit_sum = get_digit_sum(num)
            if digit_sum in dict_nums:
                ans = max(ans, num + dict_nums[digit_sum])
            dict_nums[digit_sum] = max(dict_nums[digit_sum], num)
        return ans 

# Demonstration with nums = [18, 43, 36, 13, 7]:
# - Initial: ans = -1, dict_nums = {}
# - num = 18: digit_sum = 9, dict_nums[9] = 0 -> max(0, 18) = 18, ans = -1 (no pair yet)
# - num = 43: digit_sum = 7, dict_nums[7] = 0 -> max(0, 43) = 43, ans = -1
# - num = 36: digit_sum = 9, dict_nums[9] = 18, ans = max(-1, 36 + 18) = 54, dict_nums[9] = max(18, 36) = 36
# - num = 13: digit_sum = 4, dict_nums[4] = 0 -> max(0, 13) = 13, ans = 54
# - num = 7: digit_sum = 7, dict_nums[7] = 43, ans = max(54, 7 + 43) = 54, dict_nums[7] = max(43, 7) = 43
# - Return: 54 (max sum from pair 18 + 36, both with digit sum 9)