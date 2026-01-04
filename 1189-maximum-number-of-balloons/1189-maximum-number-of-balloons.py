class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        min_count = float('inf')
        # ToDo: Write Your Code Here.
        count = {}
        for c in text:
            if c not in count:
                count[c] = 0
            count[c] += 1
        min_count = min(min_count, count.get('b', 0))
        min_count = min(min_count, count.get('a', 0))
        min_count = min(min_count, count.get('l', 0) // 2)
        min_count = min(min_count, count.get('o', 0) // 2)
        min_count = min(min_count, count.get('n', 0))
        
        return min_count