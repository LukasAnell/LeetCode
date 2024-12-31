from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        uniqueElements = []
        for num in nums:
            if num not in uniqueElements:
                uniqueElements.append(num)
        for i in range(len(uniqueElements)):
            nums[i] = uniqueElements[i]
        return len(uniqueElements)
