class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = {}
        length = 0
        oddFound = False

        for c in s:
            if c not in count:
                count[c] = 0
            count[c] += 1
        
        for key, value in count.items():
            if value % 2 == 0:
                length += value
            else:
                length += (value - 1)
                oddFound = True
        
        if oddFound:
            length += 1
        
        return length