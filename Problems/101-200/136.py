from typing import List


class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        uniqueElements = []
        for num in nums:
            if num in uniqueElements:
                uniqueElements.remove(num)
            else:
                uniqueElements.append(num)
        return uniqueElements[0]
