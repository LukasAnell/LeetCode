class Solution:
    def trailingZeroes(self, n: int) -> int:
        count = 0
        i = 5
        while n // i > 0:
            count += n // i
            i *= 5
        return count
