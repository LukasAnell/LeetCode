class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        start = 0
        maxLength = 0
        usedChar = {}
        for i, char in enumerate(s):
            if char in usedChar and start <= usedChar[char]:
                start = usedChar[char] + 1
            else:
                maxLength = max(maxLength, i - start + 1)
            usedChar[char] = i
        return maxLength
