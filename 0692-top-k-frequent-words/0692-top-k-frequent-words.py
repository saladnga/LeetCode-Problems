class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        freq = {}
        res = []
        for word in words:
            if word not in freq:
                freq[word] = 0
            freq[word] += 1
        heap = []
        for key, val in freq.items():
            heapq.heappush(heap, (-val, key))
        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        return res
