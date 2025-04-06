class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True
        s_new = ''.join(ch for ch in s.lower() if ch.isalnum())
        left = 0
        right = len(s_new) - 1
        while left < right:
            if s_new[left] != s_new[right]:
                return False
            left += 1
            right -= 1
        return True