class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        mask = x ^ y
        hamming_distance = bin(mask).count("1")
        return hamming_distance