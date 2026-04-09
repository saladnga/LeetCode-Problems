class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num < 2:
            return num == 1
        left, right = 2, num // 2
        while left <= right:
            mid = (left + right) / 2
            guess = mid * mid
            if guess == num:
                return True
            elif guess < num:
                left = mid + 1
            else:
                right = mid - 1
        return False