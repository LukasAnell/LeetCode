from typing import List


class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        hasGreatest = []
        for child in candies:
            hasGreatest += [child + extraCandies >= maxCandies]
        return hasGreatest
