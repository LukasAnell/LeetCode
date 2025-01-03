from collections import Counter
from typing import List


class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        sneakyNums = []
        numCounts = Counter(nums)
        for key, value in numCounts.items():
            if value == 2:
                sneakyNums += [key]
            if len(sneakyNums) == 2:
                break
        return sneakyNums
