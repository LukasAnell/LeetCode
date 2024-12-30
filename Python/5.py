class Solution:
    def longestPalindrome(self, s: str) -> str:
        sLen = len(s)
        if sLen == 0:
            return ""
        if sLen == 1:
            return s
        maxLength = 1
        start = 0
        for i in range(1, sLen):
            if (
                i - maxLength >= 1
                and s[i - maxLength - 1 : i + 1] == s[i - maxLength - 1 : i + 1][::-1]
            ):
                start = i - maxLength - 1
                maxLength += 2
                continue
            if (
                i - maxLength >= 0
                and s[i - maxLength : i + 1] == s[i - maxLength : i + 1][::-1]
            ):
                start = i - maxLength
                maxLength += 1
        return s[start : start + maxLength]
