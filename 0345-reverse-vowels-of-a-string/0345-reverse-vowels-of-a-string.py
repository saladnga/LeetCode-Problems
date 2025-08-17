class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['u', 'i', 'o', 'e', 'a']
        left = 0
        right = len(s) -1
        s = list(s)
        while left <= right:
            if s[left].lower() in vowels and s[right].lower() in vowels:
                s[left], s[right] = s[right], s[left]
                left += 1
                right -= 1
            elif s[left].lower() in vowels and s[right].lower() not in vowels:
                right -= 1
            else:
                left += 1
        return "".join(s)