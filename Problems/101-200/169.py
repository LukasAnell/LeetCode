from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        numsCount = {}
        for num in nums:
            numsCount[num] = numsCount.get(num, 0) + 1
        return max(numsCount.items(), key=lambda x: x[1])[0]
