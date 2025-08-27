from typing import List


class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        output = nums[:]
        for _ in range(k):
            minIndex = output.index(min(output))
            output[minIndex] = output[minIndex] * multiplier
        return output
