class Solution:
    def countSymmetricIntegers(self, low: int, high: int) -> int:
        result = 0
        for i in range(low, high + 1):
            num = str(i)
            if len(num) % 2 == 0:
                half = len(num) // 2
                first_half = num[:half]
                second_half = num[half:]
                sum1 = sum(int(ch) for ch in first_half)
                sum2 = sum(int(ch) for ch in second_half)
                if sum1 == sum2:
                    result += 1
        return result