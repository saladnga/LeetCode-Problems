class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        max_length = 0
        freq = {}
        window_start = 0
        max_freq = 0
        for window_end in range(len(s)):
            right_char = s[window_end]
            if right_char not in freq:
                freq[right_char] = 0
            freq[right_char] += 1
            max_freq = max(max_freq, freq[right_char])

            while window_end - window_start + 1 - max_freq > k:
                left_char = s[window_start]
                freq[left_char] -= 1
                window_start += 1
            
            max_length = max(max_length, window_end - window_start + 1)
        return max_length