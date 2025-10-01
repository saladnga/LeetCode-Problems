class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if len(words) == 0 or len(words[0]) == 0:
            return []

        result = []
        word_freq = {}
        word_count = len(words)
        word_length = len(words[0])

        if len(set(words)) == 1:
            word = words[0]
            word_count = len(words)
            word_length = word_count * len(word)
            for i in range(len(s) - word_length + 1):
                if s[i : i + word_length] == word * word_count:
                    result.append(i)
            return result

        for word in words:
            if word not in word_freq:
                word_freq[word] = 0
            word_freq[word] += 1
        
        for i in range(len(s) - word_count * word_length + 1):
            word_meet = {}
            for j in range(0, word_count):
                next_index = i + j * word_length
                word = s[next_index : next_index + word_length]
                if word not in word_freq:
                    break
                if word not in word_meet:
                    word_meet[word] = 0
                word_meet[word] += 1
                if word_meet[word] > word_freq.get(word, 0):
                    break
                if j + 1 == word_count:
                    result.append(i)
        return result