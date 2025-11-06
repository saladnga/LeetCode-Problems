class Solution:
    def equalSubstring(self, s: str, t: str, maxCost: int) -> int:
        window_start = 0
        curr_cost = 0
        max_len = 0
        for window_end in range(len(s)):
            curr_cost += abs(ord(s[window_end]) - ord(t[window_end]))
            while curr_cost > maxCost and window_start <= window_end:
                curr_cost -= abs(ord(s[window_start]) - ord(t[window_start]))
                window_start += 1
            max_len = max(max_len, window_end - window_start + 1)
        return max_len