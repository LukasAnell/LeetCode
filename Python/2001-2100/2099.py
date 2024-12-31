from typing import List


class Solution:
    def maxSubsequence(self, nums: List[int], k: int) -> List[int]:
        indexedNums = list(enumerate(nums))
        indexedNums.sort(key=lambda x: x[1], reverse=True)
        firstK = indexedNums[:k]
        firstK.sort(key=lambda x: x[0])
        return [x[1] for x in firstK]
