from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        if target in nums:
            first = nums.index(target)
            nums.reverse()
            last = len(nums) - 1 - nums.index(target)
        else:
            first = last = -1
        return [first, last]
