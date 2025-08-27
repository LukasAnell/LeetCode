class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        return str(bin(abs(goal ^ start)))[2:].count("1")
