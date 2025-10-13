class Solution:
    def findLeastNumOfUniqueInts(self, arr: List[int], k: int) -> int:
        freq = {}
        for num in arr:
            if num not in freq:
                freq[num] = 0
            freq[num] += 1
        
        ordered = sorted(freq.values(), reverse=True)

        while k:
            val = ordered[-1]
            if val <= k:
                k -= val
                ordered.pop()
            else:
                break
        
        return len(ordered)