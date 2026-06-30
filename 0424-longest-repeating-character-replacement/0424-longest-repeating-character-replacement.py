class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, right = 0, 1
        count = defaultdict(int)
        max_len = 0
        for right in range(len(s)):
            count[s[right]] += 1
            max_freq = max(count.values())
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
            max_len = max(max_len, right - left + 1)
        return max_len