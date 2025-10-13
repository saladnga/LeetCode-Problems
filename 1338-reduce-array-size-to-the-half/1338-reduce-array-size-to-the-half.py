class Solution:
    def minSetSize(self, arr: List[int]) -> int:
        freq = {}
        for num in arr:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        
        counts = sorted(freq.values(), reverse=True)
        ans = 0
        half = len(arr) // 2
        removed = 0

        for count in counts:
            ans += 1
            removed += count
            if removed >= half:
                return ans
        return ans
        