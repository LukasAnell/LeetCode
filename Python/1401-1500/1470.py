from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        newList = []
        for i in range(0, n):
            newList += [nums[i], nums[n + i]]
        return newList
