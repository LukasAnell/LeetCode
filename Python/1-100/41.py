from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        highest = max(max(nums), 1)
        numSet = set(nums)
        for i in range(1, highest + 1):
            if i not in numSet:
                return i
        return max(nums) + 1
