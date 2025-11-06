class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowel = ['a', 'e', 'i', 'o', 'u']
        count = 0
        for ch in s[:k]:
            if ch in vowel:
                count += 1

        max_count = count
        for i in range(k, len(s)):
            if s[i] in vowel:
                count += 1
            if s[i - k] in vowel:
                count -= 1
            max_count = max(max_count, count)
            
        return max_count