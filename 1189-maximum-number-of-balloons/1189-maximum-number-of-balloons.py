class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        count = {}
        for c in text:
            if c not in count:
                count[c] = 0
            count[c] += 1
        b_count = count.get('b', 0)
        a_count = count.get('a', 0)
        l_count = count.get('l', 0) // 2
        o_count = count.get('o', 0) // 2
        n_count = count.get('n', 0)
        return min(b_count, a_count, l_count, o_count, n_count)