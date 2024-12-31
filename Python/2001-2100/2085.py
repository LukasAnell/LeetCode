from collections import Counter
from typing import List


class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        words1Counter = Counter(words1)
        words2Counter = Counter(words2)
        count = 0
        for word in set(words1 + words2):
            if words1Counter[word] == 1 and words2Counter[word] == 1:
                count += 1
        return count
