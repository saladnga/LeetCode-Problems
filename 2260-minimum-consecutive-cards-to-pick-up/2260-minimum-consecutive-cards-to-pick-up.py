class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        last_seen = {}
        ans = float('inf')
        for i, card in enumerate(cards):
            if card in last_seen:
                ans = min(ans, i - last_seen[card] + 1)
            last_seen[card] = i
        if ans != float('inf'):
            return ans
        else:
            return -1