from typing import List


class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        indices = []
        for i in range(len(words)):
            if x in words[i]:
                indices += [i]
        return indices
