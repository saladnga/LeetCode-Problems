class Solution:
    def minWindow(self, s: str, t: str) -> str:
        freq = {}
        min_length = math.inf
        windowStart, min_start, window_length, matches = 0, 0, 0, 0
        
        for char in t:
            if char not in freq:
                freq[char] = 0
            freq[char] += 1
        
        for windowEnd in range(len(s)):
            right_char = s[windowEnd]
            if right_char in freq:
                freq[right_char] -= 1
                if freq[right_char] == 0:
                    matches += 1
            
            while matches == len(freq):
                window_length = windowEnd - windowStart + 1
                if window_length < min_length:
                    min_length = window_length
                    min_start = windowStart
                
                left_char = s[windowStart]
                windowStart += 1
                if left_char in freq:
                    if freq[left_char] == 0:
                        matches -= 1
                    freq[left_char] += 1
                
        if min_length == math.inf:
            return ""
        return s[min_start : min_start + min_length]