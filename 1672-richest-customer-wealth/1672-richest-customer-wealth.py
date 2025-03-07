class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        sum = [0] * len(accounts)
        for i in range(len(accounts)):
            total = 0
            for j in accounts[i]:
                total += j
            sum[i] = total
        max = sum[0]
        for num in sum:
            if num > max:
                max = num
        return max