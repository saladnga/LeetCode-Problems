class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # add pattern freq
        # traverse the string, decrements if met, value = 0 => matches + 1
        # if matches equals to len of the pattern, return true
        # if the end is larger than the length of the string, shrink the window, increment the freq values, decrement the match => keep the stucture

        freq = {}
        window_start = 0
        matches = 0

        for char in s1:
            if char not in freq:
                freq[char] = 0
            freq[char] += 1

        for window_end in range(len(s2)):
            right_char = s2[window_end]
            if right_char in freq:
                freq[right_char] -= 1
                if freq[right_char] == 0:
                    matches += 1
            if matches == len(freq):
                return True
            if window_end >= len(s1) - 1:
                left_char = s2[window_start]
                window_start += 1
                if left_char in freq:
                    if freq[left_char] == 0:
                        matches -= 1
                    freq[left_char] += 1
        return False