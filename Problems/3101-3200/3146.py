class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        difference = 0
        for i in range(len(s)):
            difference += abs(i - t.index(s[i]))
        return difference
