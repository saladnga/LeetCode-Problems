class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x_list = list(str(abs(x)))
        left = 0
        right = len(x_list) - 1
        while left < right:
            x_list[left], x_list[right] = x_list[right], x_list[left]
            left += 1
            right -= 1
        reverse = sign * int(''.join(x_list))
        return reverse

