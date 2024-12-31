from collections import Counter


class Solution:
    def checkAlmostEquivalent(self, word1: str, word2: str) -> bool:
        word1Counter = Counter(word1)
        word2Counter = Counter(word2)
        for i in range(0, 26):
            letter = chr(ord("a") + i)
            freq1 = word1Counter[letter] if letter in word1Counter else 0
            freq2 = word2Counter[letter] if letter in word2Counter else 0
            if abs(freq1 - freq2) > 3:
                return False
        return True
