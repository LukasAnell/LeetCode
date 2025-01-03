from typing import List


class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        return [all(char in allowed for char in word) for word in words].count(True)
