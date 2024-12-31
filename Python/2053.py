from typing import List


class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        occurrences = [char for char in arr if arr.count(char) == 1]
        if len(occurrences) < k:
            return ""
        return occurrences[k - 1]
