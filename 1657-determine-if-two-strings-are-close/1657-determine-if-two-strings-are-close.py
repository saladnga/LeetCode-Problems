class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        freq1 = [0] * 26
        freq2 = [0] * 26
        for char in word1:
            freq1[ord(char) - ord('a')] += 1
        for char in word2:
            freq2[ord(char) - ord('a')] += 1
        for i in range(26):
            if (freq1[i] == 0 and freq2[i] != 0) or (freq1[i] != 0 and freq2[i] == 0):
                return False
        freq1.sort()
        freq2.sort()
        for i in range(26):
            if freq1[i] != freq2[i]:
                return False
        return True

        # c1 = Counter(word1)
        # c2 = Counter(word2)

        # n1 = Counter([freq for freq in c1.values()])
        # n2 = Counter([freq for freq in c2.values()])
        
        # return c1 == c2 or (n1 == n2 and set(word1) == set(word2))