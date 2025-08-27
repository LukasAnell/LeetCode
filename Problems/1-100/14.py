from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for s in strs[1:]:
            while s[: len(prefix)] != prefix and prefix:
                prefix = prefix[: len(prefix) - 1]
        return prefix
